"""
Unit tests for rule module
"""

# Python Libraries
import pytest

# First Party Imports
import hangingart.rule as rule
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

#TODO: create and move to conftest.py
@pytest.fixture
def gen_spaces():
    space_params = [
    (40,20,40,20,'kitchen','S','1', 1, 1,),
    (30,15,20,15,'kitchen','W','1', 1, 1,),
    ]
    return [Space(*param) for param in space_params]


def test_horizontaldim_base(gen_spaces, gen_paintings):
    test = rule.HorizontalDimRule(gen_spaces, gen_paintings)
    test.update_grid()
    assert test.grid[0][0] == 1 
    assert test.grid[0][1] == 0
    assert test.grid[1][0] == 1
    assert test.grid[1][1] == 0


def test_verticaldim_base(gen_spaces, gen_paintings):
    test = rule.VerticalDimRule(gen_spaces, gen_paintings)
    test.update_grid()
    assert test.grid[0][0] == 1 
    assert test.grid[0][1] == 0
    assert test.grid[1][0] == 0
    assert test.grid[1][1] == 0


# def test_IndPop_space_(gen_spaces, gen_paintings):
#     test = rule.VerticalDimRule(gen_spaces, gen_paintings)
#     test.update_grid()
#     assert test.grid[0][0] == 1 
#     assert test.grid[0][1] == 0
#     assert test.grid[1][0] == 0
#     assert test.grid[1][1] == 0
# Can't test until hang painting method and curator class is formed!
