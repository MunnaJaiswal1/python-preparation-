import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

def display_weather(weather_data):
    if weather_data:
        main_info = weather_data["main"]
        weather_info = weather_data["weather"][0]

        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Description: {weather_info['description']}")
        print(f"Temperature: {main_info['temp']}°C")
        print(f"Humidity: {main_info['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Error fetching weather data.")

if __name__ == "__main__":
    # Replace 'your_api_key' with the API key you obtained from OpenWeatherMap
    api_key = "your_api_key"
    city = input("Enter the city name: ")

    weather_data = get_weather(api_key, city)

    display_weather(weather_data)
