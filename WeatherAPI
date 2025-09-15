import requests

API_KEY = '96c040611200d272a2d348008a6d52dc'# Replace with your OpenWeatherMap API key
CITY = 'Birmingham'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

#==== Build the Query Parameters ======
params = {
    'q': CITY,
    'appid': API_KEY,
    'units': 'imperial'  # or 'metric' for celcius
}

# === MAKE THE API CALL ===
response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)  # For now, just print it
else:
    print(f"Failed to fetch weather data: {response.status_code}")

