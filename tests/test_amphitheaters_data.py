#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""Nose tests for amphitheaters_data module."""

import logging
from pprint import pprint
from pleiades_amphitheaters.amphitheaters_data import AmphitheaterData
from unittest import TestCase

logger = logging.getLogger(__name__)

class Test_AmphitheaterData(TestCase):

    def test_parse(self):
        parser = AmphitheaterData()
        d = parser.read_data()
        assert isinstance(d, dict) == True
        assert len(d) == 7
        features = d['features']
        assert isinstance(features, list)
        assert len(features) == 267
        for f in features:
            assert f['type'] == 'Feature'

