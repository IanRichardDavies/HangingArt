"""
Unit tests for spaces_factory module
"""

# Python Libraries
import pytest

# First Party Imports
from hangingart.space import Space
from hangingart.spaces_factory import generate_spaces, PARAMS

def test_len_generate_spaces():
	tests = generate_spaces()
	assert len(tests) == len(PARAMS)

def test_type_generate_spaces():
	test_objs = generate_spaces()
	for obj in test_objs:
		assert isinstance(obj, Space)