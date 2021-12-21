from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen(
    "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

soup = BeautifulSoup(target, "html.parser")
with open(file="k-weather.xml", mode="a") as urlPage:
    urlPage.write("{}".format(soup))

for location in soup.select("location"):
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()