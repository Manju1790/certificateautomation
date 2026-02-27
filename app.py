from flask import Flask, render_template, request, redirect
import pandas as pd
import os

app = Flask(__name__)
FILE = "students.csv"

@app.route("/")
def home():
    if os.path.exists(FILE):
        df = pd.read_csv(FILE)
        students = df.to_dict("records")
    else:
        students = []
    return render_template("index.html", students=students)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    date = request.form["date"]
    time = request.form["time"]
    df = pd.read_excel(file)
    df["SendDate"] = date
    df["SendTime"] = time
    df["Status"] = "Pending"
    df.to_csv(FILE, index=False)
    return redirect("/")

if __name__ == "__main__":
    app.run()
