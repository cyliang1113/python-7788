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

@app.route("/login", methods=["get", "post"])
def login():
    username = ""
    password = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
    elif request.method == "GET":
        username = request.args.get("username")
        password = request.args.get("password")
        
    print username
    print password
    
    if(u"admin" == username and u"admin" == password):
        return "login success"
    return render_template("loginPage.html", message=u"用户名或者密码错误", username=username)

if __name__ == "__main__":
    app.run("", 8080, debug=True)
