# from  spark import total_income,total_expenditure,total_balance,today_income,today_expenditure
from flask import Flask, render_template,redirect, request, url_for
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import date

import os
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signup_save",methods=["POST"])
def signup_save():
    if len(request.form["pass"])>=8:
        password = generate_password_hash(request.form["pass"])
        name = request.form["name"]
        email = request.form["email"]
        return redirect(url_for("home"))


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
