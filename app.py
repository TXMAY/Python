import sys
from urllib import request
from bs4 import BeautifulSoup
from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


#@app.route("/")
#def hello():
#    return "<h1> Hello World!<h1>"

@app.route("/")
def home():
    return render_template("index.html", subject="안녕하세요. 반갑습니다. 이홍주입니다.")

@app.route("/<user>")
def hello(user):
    return "<h1> hello "+ user

@app.route("/about")
def about():
    return "about World!"

@app.route("/show1")
def show1():
    return render_template("busan1.html", subject="부산중위연령시각화")

if __name__ == "__main__":
    app.run()
