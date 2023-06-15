import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("SHEET_TOKEN")
PRICES_ENDPOINT = "https://api.sheety.co/86491734d714ce9232e2093928b5893f/flightDeals/prices"
CUSTOMERS_ENDPOINT = "https://api.sheety.co/86491734d714ce9232e2093928b5893f/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}
        self.auth = {
            "Authorization": API_KEY
        }

    def get_sheet_data(self):
        self.destination_data = requests.get(url=PRICES_ENDPOINT, headers=self.auth)
        return self.destination_data.json()["prices"]

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{PRICES_ENDPOINT}/{city['id']}", json=new_data, headers=self.auth)
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = CUSTOMERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data