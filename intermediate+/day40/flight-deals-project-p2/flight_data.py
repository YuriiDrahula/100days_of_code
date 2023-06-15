class FlightData:
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, stop_overs=0, via_city=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport

        self.stop_overs = stop_overs
        self.via_city = via_city
