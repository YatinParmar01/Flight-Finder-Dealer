import requests

SHEETY_ENDPOINTS = "https://api.sheety.co/0caeff2ba6219af264d0b0059e1ec994/finalFlightDeals/prices"
class DataManager:
    def __int__(self):
        self.destination_data = {}
    def get_destination_data(self):
         response = requests.get(url=SHEETY_ENDPOINTS)
         data = response.json()
         self.destination_data = data['prices']
         return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                        "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINTS}/{city['id']}",
                json=new_data
            )
            print(response.text)