"""
Unit tests for space module
"""

# Python Libraries
import pytest

# First Party Imports
from hangingart.painting import Painting
from hangingart.space import Space


def test_default_args():
    test = Space()
    assert test.max_hor_dim == 0.0 
    assert test.min_hor_dim == 0.0
    assert test.max_ver_dim == 0.0 
    assert test.min_ver_dim == 0.0 
    assert test.room == ''
    assert test.surface_dir == '' 
    assert test.floor == 1
    assert test.prime_flag == 1
    assert test.max_pieces == 1
    assert test.categories == None
    assert test.complete == 0
    assert test.contains_poster_flag == 0
    assert test.colours == None
    assert test.paintings_hung == None
    assert test.margin == 6.0


def test_hang():
    space = Space(
        100, 
        10,
        100,
        10,)
    painting = Painting(
        'circles',
        50,
        50,
        'abstract',
        0,
        1,
        ['blue'],)
    space.hang(painting)
    assert space.paintings_hung == [painting]
    assert space.complete
    assert space.max_hor_dim == 44.0
    assert space.max_ver_dim == 44.0
    assert space.categories == ['abstract']
    assert not space.contains_poster_flag    


def test_display(capsys):
    space = Space(
        100, 
        10,
        100,
        10,
        'kitchen',
        'S',)
    painting = Painting(
        'circles',
        50,
        50,
        'abstract',
        0,
        1,
        ['blue'],)
    space.hang(painting)
    painting.hang()
    space.display()
    captured = capsys.readouterr()
    assert 'kitchen S' in captured.out
    assert 'Y' in captured.out
    assert 'circles' in captured.out
    assert 'abstract' in captured.out

