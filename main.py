from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    for cities in sheet_data:
        cities["iataCode"] = FlightSearch().flight_data(city=cities["city"])[0]["code"]
    data_manager.result = sheet_data
    data_manager.update_sheet_data()

details = []
for cities in sheet_data:
    flight = FlightSearch().get_flight_details(destination_city=cities["iataCode"], max_price=cities["lowestPrice"])
    if flight is not None:
        if flight.price < cities["lowestPrice"]:
            notification_manager.send_sms(
                message=f"Low price alert! Only £{flight.price} to fly from "
                        f"{flight.origin_city}-{flight.origin_airport} to "
                        f"{flight.destination_city}-{flight.destination_airport}, "
                        f"from {flight.out_date} to {flight.return_date}."

            )
