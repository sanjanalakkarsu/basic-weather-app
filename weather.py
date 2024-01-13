import requests

def get_weather(api_key, location):
    url = "http://api.openweathermap.org/data/2.5/weather?"
    parameters = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  
    }

    try:
        response = requests.get(url, params=parameters)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        print("\nCurrent Weather:")
        print(f"Location: {weather_data['name']}, {weather_data['sys']['country']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        print("Unable to fetch weather data.")

if __name__ == "__main__":
    api_key = 'ba23eb1a5bfea8062f7c300ef4eff6d2'  
    location = input("Enter city or ZIP code: ")

    # Fetch and display weather data
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)