"""
Unit tests for space module
"""

# Python Libraries
import pytest

# First Party Imports
from hangingart.painting import Painting
from hangingart.space import Space

#TODO: create and move to conftest.py
@pytest.fixture
def gen_paintings():
    painting_params = [
    ('Several Circles',30,30,'pop art',1,1,['black','purple','blue',],),
    ('Transformation',50,70,'indigenous',1,1,['orange','brown','blue',],),
    ]
    return [Painting(*param) for param in painting_params]


def test_default_args():
    test = Painting()
    assert test.name == ''
    assert test.horizontal_dim == 0.0 
    assert test.vertical_dim == 0.0
    assert test.category == '' 
    assert test.poster == 0
    assert test.prime_flag == 1
    assert test.complete == 0
    assert test.colours == None


def test_hang():
    painting = Painting()
    painting.hang()
    assert painting.complete


def test_display(gen_paintings, capsys):
    for painting in gen_paintings:
        painting.display()
    captured = capsys.readouterr()
    assert 'Several Circles' in captured.out
    assert 'Transformation' in captured.out
    assert 'pop art' in captured.out
    assert 'indigenous' in captured.out

