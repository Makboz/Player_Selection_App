import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


ROLES = [
    "Batsman",
    "Bowler",
    "All-rounder"
]

STATUS = [
    "Selected",
    "Under Consideration",
    "Rejected"
]


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///players.db")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("full_name")
        age = request.form.get("age")
        height = request.form.get("height")
        role = request.form.get("role")
        rating = request.form.get("rating")
        coach_comment = request.form.get("comments")
        status = request.form.get("status")

        db.execute("INSERT INTO players (full_name, age, height, role, rating, comments, selected) VALUES(?, ?, ?, ?, ?, ?, ?)",
                   name, age, height, role, rating, coach_comment, status)
        flash("Player Portfolio Successfully Updated")
        return redirect("/")

    else:
        players = db.execute("SELECT * FROM players")
        return render_template("index.html", players=players, roles=ROLES, statuses=STATUS)


@app.route("/delete", methods=["POST"])
def delete():
    db.execute("DELETE FROM players WHERE full_name = ?", [request.form['full_name']])
    flash("Player Portfolio Successfully Updated")
    return redirect("/")
