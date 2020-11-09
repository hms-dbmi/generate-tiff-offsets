#!/usr/bin/env python

"""Tests for `generate_tiff_offsets` package."""


import unittest
import json

from generate_tiff_offsets.generate_tiff_offsets import generate_tiff_offsets


class TestGenerate_tiff_offsets(unittest.TestCase):
    """Tests for `generate_tiff_offsets` package."""

    def test_offsets(self):
        generate_tiff_offsets('./tests/test-input/multi-channel.ome.tif')
        with open('./tests/test-output-expected/multi-channel.offsets.json', 'r') as f:
            expected = json.loads(f.read())
        with open('./tests/test-input/multi-channel.offsets.json', 'r') as f:
            actual = json.loads(f.read())
        assert(actual == expected)
