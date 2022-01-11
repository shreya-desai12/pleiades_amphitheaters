#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch data from sfheath's Github repository URI
"""

import requests
import json

class ParseData:
    """
    Fetch sfheath amphitheater data over the web and return parsed JSON.
    """

    def read_data(self):
        """
        Perform fetch and parse.
        
        :returns: the fetched JSON data
        :rtype: dict or list
        """
        response = requests.get('https://raw.githubusercontent.com/roman-amphitheaters/roman-amphitheaters/main/roman-amphitheaters.geojson')
        if response.status_code == 200:
            # print(response.status_code)
            json_data = json.loads(response.text)
            # print(type(json_data))   
            # print(json_data)             
            return json_data
        else:
            print("Error in retrieving the data")
            return {}
        
rd = ParseData()
final_data = rd.read_data()

