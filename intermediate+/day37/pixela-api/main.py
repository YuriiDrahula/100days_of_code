import requests
from datetime import datetime

USERNAME = "yuriid97"
TOKEN = "jgjdugsds42ighk@hgjuhe"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users/"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_endpoint = f"{pixela_endpoint}{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
today_formatted_date = today.strftime("%Y%m%d")
print(today_formatted_date)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you learn code today? ")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}{USERNAME}/graphs/{GRAPH_ID}/{today_formatted_date}"

update_pixel_config = {
    "quantity": "3.2"
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}{USERNAME}/graphs/{GRAPH_ID}/20220408"
# response = requests.delete(url=delete_endpoint, headers=headers)
