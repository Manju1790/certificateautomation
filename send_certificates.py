import pandas as pd
from datetime import datetime
import os

def generate_certificate(name):
    os.makedirs("certificates", exist_ok=True)
    path=f"certificates/{name}.pdf"
    with open(path,"w") as f:
        f.write(f"Certificate for {name}")
    return path

def send_certificate(email, path):
    print(f"Sending {path} to {email}")

if os.path.exists("students.csv"):
    df = pd.read_csv("students.csv")
    now=datetime.now()
    d=now.strftime("%Y-%m-%d")
    t=now.strftime("%H:%M")

    for i,row in df.iterrows():
        if row["Status"]=="Pending":
            if row["SendDate"]==d and row["SendTime"]==t:
                pdf=generate_certificate(row["Name"])
                send_certificate(row["Email"], pdf)
                df.at[i,"Status"]="Sent"

    df.to_csv("students.csv", index=False)
