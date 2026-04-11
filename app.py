# from  spark import total_income,total_expenditure,total_balance,today_income,today_expenditure
from flask import Flask, render_template,redirect, request, url_for
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import date
from database import conn

import os
import csv

cursor=conn.cursor()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/signup")
def signup():
    val=0
    email_info=""
    return render_template("signup.html",val=val,email_info=email_info)

@app.route("/signup_save",methods=["POST"])
def signup_save():
    if len(request.form["pass"])>=8:
        password = generate_password_hash(request.form["pass"])
        name = request.form["name"]
        email = request.form["email"]
        username= request.form["username"]
        cursor.execute("SELECT 1 FROM users WHERE Email=%s",(email,))
        result=cursor.fetchone()
        if result is None:

            cursor.execute("""CREATE TABLE IF NOT EXISTS users(id int AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(20) NOT NULL,
                Email VARCHAR(50) NOT NULL,
                Username VARCHAR(20) NOT NULL,
                Password VARCHAR(10000) NOT NULL
                )""")
            conn.commit()
            cursor.execute("INSERT INTO users(Name,Email,Username,Password) VALUES(%s,%s,%s,%s)",
                       (name,email,username,password))
            conn.commit()
            return redirect(url_for("home"))
        else:
            email_info=f"{email} is used before"
            return redirect(url_for("signup",email_info=email_info))
    else:
        val=int(1)
        return  redirect((url_for("signup",val=val)))


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
