import requests

API_KEY = 'PWMS4M43677PWAPJ6LW7SMCLV'

LOCATION = "Kyiv"

# Make the API request
url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{LOCATION}'
params = {
    'unitGroup': 'us',
    'key': API_KEY,
    'include': 'hours'
}
response = requests.get(url, params=params)


data = response.json()['days'][0]['hours']
for hour in data[:12]:
    print(f"{hour['datetime']}: {hour['conditions']}, {hour['temp']}\u00b0F")
