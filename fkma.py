from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/")
def hello():
    target = request.urlopen(
        "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

    soup = BeautifulSoup(target, "html.parser")

    output = ""
    for location in soup.select("location"):
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}</br>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}".format(location.select_one(
            "tmn").string, location.select_one("tmx").string)
        output += "<hr/>"

    return output
