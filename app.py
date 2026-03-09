from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/input", methods=["GET", "POST"])
def input_task():
    if request.method == "GET":
        projects = set()
        with open("tasks.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                projects.add(row["project_title"])
        return render_template("input.html", projects=sorted(projects))
    
    else:
        project_title = request.form["project_title"]
        title = request.form["title"]
        description = request.form["description"]
        status = request.form["status"]
        next_steps = request.form["next_steps"]
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open("tasks.csv", "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["datetime", "project_title", "title", "description", "status", "next_steps"])
            writer.writerow({
                "datetime": timestamp,
                "project_title": project_title,
                "title": title,
                "description": description,
                "status": status,
                "next_steps": next_steps
            })
        
        return redirect(url_for("display"))

@app.route("/display")
def display():
    tasks = []
    with open("tasks.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tasks.append(row)
    return render_template("display.html", tasks=tasks)

