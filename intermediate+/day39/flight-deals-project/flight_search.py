import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta
from flight_data import FlightData

load_dotenv()
TEQUILA_API = os.getenv("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"

now = datetime.today()
add_six_months = now + timedelta(days=182)
current_date = now.strftime("%d/%m/%Y")
six_month_later_date = add_six_months.strftime("%d/%m/%Y")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.city_codes = []

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        self.city_codes.append(code)
        return self.city_codes

    def search_for_flight(self, from_city_code, to_city_code):
        endpoint = f"{TEQUILA_ENDPOINT}/search"
        headers = {"apikey": TEQUILA_API}
        query = {"fly_from": from_city_code,
                 "fly_to": to_city_code,
                 "date_from": current_date,
                 "date_to": six_month_later_date,
                 "nights_in_dst_from": 7,
                 "nights_in_dst_to": 28,
                 "flight_type": "round",
                 "one_for_city": 1,
                 "max_stopovers": 0,
                 "curr": "USD"
                 }

        response = requests.get(url=endpoint, params=query, headers=headers)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {to_city_code}.")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data

