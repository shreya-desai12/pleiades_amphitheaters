#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for the data module"""

import logging
from pleiades_amphitheaters.data import DataFetcher
from unittest import TestCase

logger = logging.getLogger(__name__)

class Test_DataFetcher(TestCase):

    def test_pleiades_uri(self):
        uri = 'https://pleiades.stoa.org/places/39414/json'
        df = DataFetcher()
        data = df.read_data(uri)
        assert isinstance(data, dict) == True
