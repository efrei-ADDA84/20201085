import os
import requests

def get_weather(latitude, longitude):
    api_key = os.getenv("key")
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        raise Exception(f"Failed to retrieve weather data: {data['message']}")

if __name__ == "__main__":
    latitude =  os.getenv('latitude')
    longitude = os.getenv('longitude')

    try:
        weather_data = get_weather(latitude, longitude)
        print("Weather data:")
        print(weather_data)
    except Exception as e:
        print(f"Error: {e}")
