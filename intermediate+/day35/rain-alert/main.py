import requests
from twilio.rest import Client

MY_LAT = 48.177269
MY_LONG = 23.296431
OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "ae517d00f4ac76f061dd01f0c430c5dd"
account_sid = "AC6153ef3c83fe8e67f4346bcd5be54e7f"
auth_token = "ebd84da1ce156c50d823b91b0bc25905"

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_ENDPOINT, params=params)
response.raise_for_status()
data = response.json()

# print(data)
# print(data["hourly"][0]["weather"][0]["id"])

weather_data = data["hourly"][:12]
will_rain = False

for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella☂",
        from_="+15856011936",
        to="+380686600977"
    )
