#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""Nose tests for amphitheaters_data module."""

import logging
from pathlib import Path
from pprint import pprint
from pleiades_amphitheaters.amphitheaters_data import ParseData
from unittest import TestCase

logger = logging.getLogger(__name__)
test_data_path = Path('tests/data').resolve()


def setup_module():
    """Change me"""
    pass


def teardown_module():
    """Change me"""
    pass


class Test_ParseData(TestCase):

    def setUp(self):
        """Change me"""
        pass

    def tearDown(self):
        """Change me"""
        pass

    def test_parse(self):
        parser = ParseData()
        d = parser.read_data()
        assert isinstance(d, dict) == True
        assert len(d) == 7
        features = d['features']
        assert isinstance(features, list)
        assert len(features) == 267
        for f in features:
            assert f['type'] == 'Feature'

