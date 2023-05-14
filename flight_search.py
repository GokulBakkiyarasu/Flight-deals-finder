from requests import *
from datetime import datetime, timedelta
from flight_data import FlightData
header = {
    "apikey": "your Kiwi.com API key"
}
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query?"
TEQUILA_ENDPOINT1 = "https://api.tequila.kiwi.com/v2/search?"


class FlightSearch:
    def __init__(self):
        self.city = None
        self.destination = None
        self.max_price = 0
        self.from_date = datetime.now().date().strftime("%d/%m/%Y")
        self.to_date = (datetime.now().date() + timedelta(days=180)).strftime("%d/%m/%Y")

    def flight_data(self, city):
        self.city = city
        parameter = {
            "term": self.city,
            "location_types": "city",
        }
        response = get(url=TEQUILA_ENDPOINT, params=parameter, headers=header)
        result = response.json()["locations"]
        return result

    def get_flight_details(self, destination_city, max_price):
        self.destination = destination_city
        self.max_price = max_price
        parameters = {
            "fly_from": "LON",
            "fly_to": self.destination,
            "date_from": self.from_date,
            "date_to": self.to_date,
            "price_from": 0,
            "price_to": self.max_price,
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
        }
        response = get(url=TEQUILA_ENDPOINT1, params=parameters, headers=header)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {self.destination}.")
            return None
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data


