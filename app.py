from flask import Flask, render_template,redirect, request, url_for
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import date
from database import get_connection,calculations,enter_new_entry,get_conn
from mail import  mail,send_mail
from apscheduler.schedulers.background import BackgroundScheduler

import  threading

today_date=date.today()
app = Flask(__name__)
scheduler=BackgroundScheduler()
scheduler.add_job(send_mail,trigger='cron',hour=23,minute=56,timezone="Asia/Kolkata")
scheduler.start()

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/check_login", methods=["POST"])
def check_login():
    username=request.form.get("username")
    password=request.form.get("pass")
    result=get_conn(username)
    if result is None:
        return redirect(url_for("home"))
    try:
        name = result[1]
        if check_password_hash(result[-1], password):
            if result[2]==username or result[3]==username:
                return  redirect(url_for(f"login_done",name=name))
            return redirect(url_for("home"))
        return redirect(url_for("home"))
    except Exception as e:
        return redirect(url_for("home"))

@app.route("/login_done/<name>")
def login_done(name):
    total_income,total_expenditure,total_balance,data=calculations(name)
    return render_template("index.html",name=name,
                                   total_income=total_income or 0,total_expenditure=total_expenditure or 0,
                                   total_balance=total_balance or 0,data=data,today_date=today_date)

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
        conn = get_connection()
        cursor = conn.cursor()
        password = generate_password_hash(request.form["pass"])
        name = request.form["name"]
        email = request.form["email"]
        username= request.form["username"]
        threading.Thread(target=mail,args=(email,name))
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
                       (username,email,name,password))
            conn.commit()
            conn.close()
            cursor.close()
            return redirect(url_for("home"))
        else:
            return redirect(url_for("signup"))
    else:
        return  redirect(url_for("signup"))

@app.route("/demo")
def demo():
    return redirect(url_for("login_done",name='Demo'))

if __name__ == "__main__":
    app.run(debug=True)