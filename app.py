from flask import Flask, render_template, request, redirect
import requests
from os import getenv


API_KEY = getenv("API_KEY")
if not API_KEY:
    raise("API Key not set")


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather")
def weather():
    city_id = request.args.get("id")
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}&units=metric&lang=pt_br").json()
    return render_template("weather.html", weather=weather)

@app.route("/search")
def search():
    city = request.args.get("city")
    if not city:
        return render_template("index.html", error="Search returned no results")
    find = requests.get(f"https://api.openweathermap.org/data/2.5/find?q={city}&appid={API_KEY}&units=metric&lang=pt_br").json()
    return render_template("index.html", cities=find["list"])
