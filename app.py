from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        print("Haetaan säätä kaupungille:", city)
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=fi"
        print("Käytetty URL:", url)
        response = requests.get(url)
        print("Status code:", response.status_code)
        print("Response:", response.text)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "kaupunki": data["name"],
                "lämpötila": data["main"]["temp"],
                "kuvaus": data["weather"][0]["description"],
                "ikoni": data["weather"][0]["icon"]
            }
        else:
            weather_data = {"error": "Kaupunkia ei löytynyt 😢"}

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
