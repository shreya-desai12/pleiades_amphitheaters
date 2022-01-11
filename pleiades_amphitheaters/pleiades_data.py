#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch Pleiades JSON serialization for an individual Pleiades place resource
"""

from pleiades_amphitheaters.data import DataFetcher

class PleiadesData(DataFetcher):
    """
    Fetch Pleiades Place data over the web and return parsed JSON.
    """

    def read_data(
        self,
        uri: str
    ):
        return DataFetcher.read_data(self, uri=uri)
