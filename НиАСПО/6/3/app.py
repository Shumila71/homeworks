from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_weather():
    api_key = '295ff2d2578aaf6f3f6f335755ebb08b'  
    city = 'Moscow'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/')
def index():
    weather_data = get_weather()
    location = weather_data.get('name', 'Unknown')
    temperature = weather_data['main']['temp']
    weather_description = weather_data['weather'][0]['description']
    return render_template('index.html', location=location, temperature=temperature, weather_description=weather_description)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
