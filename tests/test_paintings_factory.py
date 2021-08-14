"""
Unit tests for paintings_factory module
"""

# Python Libraries
import pytest

# First Party Imports
from hangingart.painting import Painting
from hangingart.paintings_factory import generate_paintings, PARAMS


def test_len_generate_paintings():
	tests = generate_paintings()
	assert len(tests) == len(PARAMS)


def test_type_generate_paintings():
	test_objs = generate_paintings()
	for obj in test_objs:
		assert isinstance(obj, Painting)