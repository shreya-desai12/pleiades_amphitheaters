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
        base_uri = 'https://pleiades.stoa.org/places/'
        if not uri.startswith(base_uri):
            raise ValueError(
                f'Expected a Pleiades URI starting with {base_uri}. Got {uri}.')
        return DataFetcher.read_data(self, uri=uri)
