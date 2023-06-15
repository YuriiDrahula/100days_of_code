import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
BEARER_AUTH = os.getenv("BEARER_AUTH")


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("Type which exercise have you done?: ")

headers_params = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

request_body = {
    "query": exercise_input,
    "gender": "mail",
    "weight_kg": 74.5,
    "height_cm": 178.00,
    "age": 25
}

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

response = requests.post(url=exercise_endpoint, json=request_body, headers=headers_params)
data = response.json()["exercises"]

bearer_auth = {
    "Authorization": BEARER_AUTH
}

for exercise in data:
    new_row = {
        "date": date,
        "time": time,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
        "id": exercise["tag_id"]
    }

    workout = {
        "workout": new_row
    }

    sheet_endpoint = "https://api.sheety.co/86491734d714ce9232e2093928b5893f/myWorkouts/workouts"
    post_row = requests.post(url=sheet_endpoint, json=workout, headers=bearer_auth)
    print(post_row.text)
    print(post_row.json())

# sheet_endpoint = "https://api.sheety.co/86491734d714ce9232e2093928b5893f/myWorkouts/workouts"
# get_sheet = requests.get(url=sheet_endpoint)
# print(get_sheet.json())


