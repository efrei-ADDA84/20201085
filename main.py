import os
import requests

def get_weather(latitude, longitude):
    api_key = "aaca89a14b3698bbd46dd966b2fa436d"
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        raise Exception(f"Failed to retrieve weather data: {data['message']}")

if __name__ == "__main__":
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))

    try:
        weather_data = get_weather(latitude, longitude)
        print("Weather data:")
        print(weather_data)
    except Exception as e:
        print(f"Error: {e}")
