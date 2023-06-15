from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

FROM_CITY = "LON"
data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()


for destination in sheet_data:
    flight = flight_search.search_for_flight(FROM_CITY, destination["iataCode"])

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        data_manager.update_destination_codes()

    if flight.price < sheet_data[destination]["price"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} " \
                  f"to {flight.destination_city}-{flight.destination_airport}"
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."


        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}"
        notification_manager.send_emails(emails, message, link)
