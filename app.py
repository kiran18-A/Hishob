from flask import Flask, render_template,redirect, request, url_for
from datetime import date

import os
import csv

app = Flask(__name__)

@app.route("/")
def home():
    name="Kiran"
    data=[]
    if os.path.exists("data.csv"):
        with open("data.csv", newline="") as file:
            reader = csv.DictReader(file)
            data = list(reader)
    data=data[-5:]
    return render_template("index.html",name=name,data=data)


@app.route("/submit", methods=["POST"])
def submit():
    today = date.today()
    entry_type = request.form["type"]
    money = request.form["money"]
    note = request.form["note"]
    file_exists = os.path.isfile("data.csv")

    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)

        # write header only once
        if not file_exists:
            writer.writerow(["Date","Amount", "Type", "Note"])

        writer.writerow([today,money,entry_type,note])

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=False)
