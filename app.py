from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# OpenWeatherMap API Key (must be set in environment variable)
API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    raise RuntimeError("OPENWEATHER_API_KEY environment variable is not set!")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    
    url = (
        "http://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    data = None
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            payload = resp.json()
            data = {
                "temp": payload["main"]["temp"],
                "desc": payload["weather"][0]["description"].title(),
                "icon": payload["weather"][0]["icon"],
            }
        else:
            data = {"temp": "?", "desc": "City not found", "icon": "01d"}
    except requests.RequestException:
        data = {"temp": "?", "desc": "Weather service error", "icon": "01d"}
    
    return render_template('index.html', weather=data, city=city)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
