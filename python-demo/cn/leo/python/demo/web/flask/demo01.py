# coding: utf-8

from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=["get"])
def home():
    return render_template("home.html")

@app.route("/login/page", methods=["get"])
def loginPage():
    return render_template("loginPage.html")

@app.route("/login", methods=["post"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if("admin" == username and "admin" == password):
        return "login success"
    return render_template("loginPage.html", message='Bad username or password', username=username)

if __name__ == "__main       __":
    app.run("", 8080, debug=True)
