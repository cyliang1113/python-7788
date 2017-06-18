# coding: utf-8

from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=["get", "post"])
def home():
    return render_template("home.html")

@app.route("/loginPage", methods=["get", "post"])
def loginPage():
    return render_template("loginPage.html")

@app.route("/login", methods=["get", "post"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if("admin" == username and "admin" == password):
        return "login success"
    return render_template("loginPage.html", message='Bad username or password', username=username)

if __name__ == "__main__":
    app.run("", 8080)