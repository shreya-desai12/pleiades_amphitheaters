#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch Pleiades JSON serialization for an individual Pleiades place resource
"""

import logging
from pleiades_amphitheaters.data import DataFetcher
import re

logger = logging.getLogger(__name__)

class PleiadesData(DataFetcher):
    """
    Fetch Pleiades Place data over the web and return parsed JSON.
    """

    def read_data(
        self,
        uri: str
    ):
        base_uri = 'https://pleiades.stoa.org/places/'
        m = re.fullmatch(base_uri + r'\d+/json', uri)
        if m is None:
            m = re.fullmatch(base_uri + r'\d+', uri)
            logger.warning(
                f'Expected Pleiades place JSON URI but got simple place URI ({uri}). '
                'Appending "/json".')
            this_uri = uri + '/json'
        else:
            this_uri = uri
        return DataFetcher.read_data(self, uri=this_uri)
