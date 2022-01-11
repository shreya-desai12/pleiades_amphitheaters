#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch data from sfheath's Github repository URI
"""

from pleiades_amphitheaters.data import DataFetcher

class AmphitheaterData(DataFetcher):
    """
    Fetch sfheath amphitheater data over the web and return parsed JSON.
    """

    def read_data(
        self,
        uri='https://raw.githubusercontent.com/roman-amphitheaters/roman-amphitheaters/main/roman-amphitheaters.geojson'
    ):
        """
        Perform fetch and parse of sfheath amphitheater data.
        
        :returns: the fetched JSON data
        :rtype: dict or list
        """
        return DataFetcher.read_data(self, uri=uri)

