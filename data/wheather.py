import os

import requests
from dotenv import load_dotenv


load_dotenv()


def get_weather(city: str = "Odesa"):
    api_key = os.getenv("WEATHER_API")
    url = f"https://api.weatherapi.com/v1/current.json?q={city}&key={api_key}"
    response = requests.get(url).json()
    weather = {
        "temp": response.get("current", {}).get("temp_c"),
        "text": response.get("current", {}).get("condition", {}).get("text"),
        "icon": response.get("current", {}).get("condition", {}).get("icon"),
        "city": city
    }
    return weather
