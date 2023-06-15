import requests
from datetime import datetime
import smtplib

MY_LAT = 48.177269
MY_LONG = 23.296431
MY_EMAIL = "ydtest97@hotmail.com"
MY_PASSWORD = "usmneuyhwbglmeqd"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour

if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5\
        and (current_hour >= sunset or current_hour <= sunrise):

    with smtplib.SMTP(host="smtp.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_PASSWORD,
            to_addrs="ydtest17@yahoo.com",
            msg="Subject:LOOK UP!\n\n"
                "The International Space Station is above you and you can see it in the sky"
        )
