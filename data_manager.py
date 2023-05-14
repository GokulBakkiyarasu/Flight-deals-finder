
from requests import *
SHEETY_ENDPOINT = "https://api.sheety.co/a08202321f292c75750cecec333eb2e7/flightDeals/prices"
header = {
    "Authorization": "your Google Sheets API token"
}


class DataManager:
    def __init__(self):
        self.result = {}

    def get_sheet_data(self):
        response = get(url=SHEETY_ENDPOINT, headers=header)
        self.result = response.json()["prices"]
        return self.result

    def update_sheet_data(self):
        for cities in self.result:
            new_data = {
                "price": {
                    "iataCode": cities["iataCode"]
                }
            }
            response = put(url=f"{SHEETY_ENDPOINT}/{cities['id']}", json=new_data, headers=header)
            print(response.text)

