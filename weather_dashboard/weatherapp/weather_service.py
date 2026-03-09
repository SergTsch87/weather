from dotenv import load_dotenv
import requests
import os


def get_weather_data(city):
    load_dotenv()
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    # url = f"https://api.openweathermap.org/data/3.0/weather?q={city}&units=metric&appid={api_key}"

    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f'Error fetching weather data: {e}')
        return None