"""
Tests for geomAnalysis.py
"""

import geomAnalysis as ga
import pytest

def test_calculateDistance():

    coord1 = [0, 0, 2]
    coord2 = [0, 0, 0]

    observed = ga.calculateDistance(coord1, coord2)

    assert observed == 2.0

def test_bondCheckFalse():
    assert ga.bondCheck(0.0) == False

def test_bondCheckTrue():
    assert ga.bondCheck(1.0) == True

def test_bondCheckType():
    bondDistance = 'a'

    with pytest.raises(TypeError):
        observed = ga.bondCheck(bondDistance)
