from flask import Flask, render_template,redirect, request, url_for
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import date
from database import conn,calculations,enter_new_entry
# from spark import pdf_data

# import threading
import os
import csv

today_date=date.today()
cursor=conn.cursor()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/check_login", methods=["POST"])
def check_login():
    username=request.form["username"]
    password=request.form["pass"]
    cursor.execute("SELECT * FROM users WHERE Email=%s OR Username=%s", (username,username,))
    result = cursor.fetchone()
    name=result[1]
    if check_password_hash(result[-1], password):
        if result[2]==username or result[3]==username:
         return  redirect(url_for(f"login_done",name=name))
    return redirect("/")

@app.route("/login_done/<name>")
def login_done(name):
    total_income,total_expenditure,total_balance=calculations(name)
    return render_template("index.html",name=name,
                                   total_income=total_income,total_expenditure=total_expenditure,
                                   total_balance=total_balance)

@app.route("/entry/<name>",methods=["POST"])
def entry(name):
    amount=request.form["money"]
    types = request.form["type"]
    note = request.form["note"]
    enter_new_entry(today_date,amount,types,note,name)
    return redirect(url_for(f"login_done",name=name))

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signup_save",methods=["POST"])
def signup_save():
    if len(request.form["pass"])>=8:
        password = generate_password_hash(request.form["pass"])
        name = request.form["name"]
        email = request.form["email"]
        username= request.form["username"]
        cursor.execute("SELECT 1 FROM users WHERE Email=%s or Username=%s",(email,username))
        result=cursor.fetchone()
        if result is None:
            cursor.execute("""CREATE TABLE IF NOT EXISTS users(id int AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(20) NOT NULL,
                Email VARCHAR(50) NOT NULL,
                Type VARCHAR(20) NOT NULL,
                Password VARCHAR(10000) NOT NULL
                )""")
            conn.commit()
            cursor.execute("INSERT INTO users(Name,Email,Username,Password) VALUES(%s,%s,%s,%s)",
                       (name,email,username,password))
            conn.commit()
            return redirect(url_for("/"))
        else:
            return redirect(url_for("signup"))
    else:
        return  redirect(url_for("signup"))


@app.route("/submit", methods=["POST"])
def submit():
    today = date.today()
    entry_type = request.form["type"]
    money = request.form["money"]
    note = request.form["note"]
    file_exists = os.path.isfile("data/data.csv")

    with open("data/data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        # write header only once
        if not file_exists:
            writer.writerow(["Date","Amount", "Type", "Note"])
        writer.writerow([today,int(money),entry_type,note])
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=False)