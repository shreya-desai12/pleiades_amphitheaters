#Pleiades JSON serialization for an individual Pleiades place resource

import requests

class Data:
    def read(self):
        response = requests.get('https://pleiades.stoa.org/places/39414/')
        if response.status_code == 200:
            json_data = response.json()
            return json_data
        else:
             print("Error in retrieving data")
             return None

r = Data()
Store = r.read()