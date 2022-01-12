#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""Nose tests for pleiades_data module."""

import logging
from pprint import pprint
from pleiades_amphitheaters.pleiades_data import PleiadesData
from unittest import TestCase

logger = logging.getLogger(__name__)

class Test_PleiadesData(TestCase):

    def test_parse(self):
        parser = PleiadesData()
        d = parser.read_data(uri='https://pleiades.stoa.org/places/39414/json')
        assert isinstance(d, dict) == True
        print(d['@type'])
        assert d['@type'] == 'Place'

    def test_parse_json_omitted(self):
        parser = PleiadesData()
        d = parser.read_data(uri='https://pleiades.stoa.org/places/39414')
        assert isinstance(d, dict) == True
        print(d['@type'])
        assert d['@type'] == 'Place'

    def test_not_pleiades(self):
        parser = PleiadesData()
        with self.assertRaises(ValueError):
            parser.read_data(uri='http://nowhere.com')

