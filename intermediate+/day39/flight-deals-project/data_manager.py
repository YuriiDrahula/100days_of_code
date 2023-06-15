import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("SHEET_TOKEN")
SHEET_ENDPOINT = "https://api.sheety.co/86491734d714ce9232e2093928b5893f/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.auth = {
            "Authorization": API_KEY
        }

    def get_sheet_data(self):
        self.destination_data = requests.get(url=SHEET_ENDPOINT, headers=self.auth)
        return self.destination_data.json()["prices"]

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", json=new_data, headers=self.auth)
            print(response.text)
