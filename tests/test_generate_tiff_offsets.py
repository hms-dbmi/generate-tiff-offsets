#!/usr/bin/env python

"""Tests for `generate_tiff_offsets` package."""
import json

from generate_tiff_offsets.generate_tiff_offsets import generate_tiff_offsets

def test_offsets():
    generate_tiff_offsets('./tests/test-input/multi-channel.ome.tif')
    with open('./tests/test-output-expected/multi-channel.offsets.json', 'r') as f:
        expected = json.loads(f.read())
    with open('./tests/test-input/multi-channel.offsets.json', 'r') as f:
        actual = json.loads(f.read())
    assert(actual == expected)
