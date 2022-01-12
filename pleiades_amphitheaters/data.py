#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Define a superclass for fetching JSON data over the web
"""

import requests

class DataFetcher:
    """
    Superclass for fetching JSON data over the web
    """

    def read_data(self, uri: str):
        """
        Perform fetch and parse.
        
        :returns: the fetched JSON data
        :rtype: dict or list
        """
        if not isinstance(uri, str):
            raise TypeError(f'Expected uri of type str. Got {type(uri)}.')
            
        response = requests.get(uri)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
        
