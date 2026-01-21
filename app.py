from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Mock API Key (Replace with real key)
API_KEY = "mock_api_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    
    # Mock Data for demonstration since we don't have a real API key active
    # In production: url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    mock_weather = {
        'Seoul': {'temp': 24, 'desc': 'Sunny', 'icon': '01d'},
        'London': {'temp': 15, 'desc': 'Rainy', 'icon': '09d'},
        'New York': {'temp': 20, 'desc': 'Cloudy', 'icon': '03d'}
    }
    
    # Simple fuzzy match or default
    data = mock_weather.get(city, {'temp': 22, 'desc': 'Clear', 'icon': '01d'})
    
    return render_template('index.html', weather=data, city=city)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
