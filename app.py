from flask import Flask, render_template,redirect, request, url_for
from datetime import date

import os
import csv

app = Flask(__name__)

def calculation():
    if os.path.exists("data/data.csv"):
        with open("data/data.csv", newline="") as file:
            reader = csv.DictReader(file)
            data = list(reader)
    total_income = 0
    total_expenditure = 0
    total_balance = 0
    for i in data:
        if i['Type']=='Income':
            total_income=total_income+int(i['Amount'])
        elif i['Type']=='Expense':
            total_expenditure=total_expenditure+int(i['Amount'])
        else:
            pass
    total_balance=total_income-total_expenditure
    return total_income,total_balance,total_expenditure

def result():
    total_income,total_balance,total_expenditure=calculation()
    return total_income,total_expenditure,total_balance

@app.route("/")
def home():
    total_income,total_expenditure,total_balance=result()
    name="Kiran"
    data=[]
    if os.path.exists("data/data.csv"):
        with open("data/data.csv", newline="") as file:
            reader = csv.DictReader(file)
            data = list(reader)
    data=data[-5:]
    return render_template("index.html",name=name,data=data,total_income=total_income,total_expenditure=total_expenditure,total_balance=total_balance)

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
    calculation()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=False)
