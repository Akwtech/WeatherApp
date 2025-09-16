import requests

API_KEY = '96c040611200d272a2d348008a6d52dc'# Replace with your OpenWeatherMap API key
CITY = 'Birmingham'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

#==== Build the Query Parameters ======
#==== Builds a dictionary of the key-value pairs that make up the API query ====#
params = {
    'q': CITY,
    'appid': API_KEY,
    'units': 'imperial'  # or 'metric' for celcius
}

# === MAKE THE API CALL ===
# === reaches out to internet, contacts OpenWeatherMap API, sends the City + API key, receives fresh data ===#
response = requests.get(BASE_URL, params=params)

if response.status_code == 200: #=== If the server call is successful ===#
    data = response.json() #=== Convert the response to JSON ===#
    #==print(data)  # For now, just print it
    #== Lets print specific fields ===#
    #==print(f"City: {data['name']}")
    #==print(f"Temperature: {data['main']['temp']}°F")
    #==print(f"Description: {data['weather'][0]['description']}")
    city = data.get("name")
    country = data.get("sys", {}).get("country")
    temp = data.get("main", {}).get("temp")
    feels_like = data.get("main", {}).get("feels_like")
    
    # == print data ===#
    print(f"Current Weather in {city}, {country}:")
    print(f"  Temperature:     {temp}°F")
    print(f"  Feels Like:      {feels_like}°F")
else:
    print(f"Failed to fetch weather data: {response.status_code}")

