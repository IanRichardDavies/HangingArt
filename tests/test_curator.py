"""
Unit tests for curator module
"""

# Python Libraries
import pytest

# First Party Imports
import hangingart.rule as rule
from hangingart.curator import Curator
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

#TODO: create and move to conftest.py
@pytest.fixture
def gen_rules():
    return [
        rule.HorizontalDimRule(),
        rule.VerticalDimRule(),
    ]


def test_create_grid(gen_rules, gen_spaces, gen_paintings):
    test = Curator(gen_rules, gen_spaces, gen_paintings)
    assert test.rules_grid.shape == (2,2,2)

def test_update_rule_grid(gen_rules, gen_spaces, gen_paintings):
    test = Curator(gen_rules, gen_spaces, gen_paintings)
    test._update_rule_grid()
    assert test.rules_grid[0][0][0] == 1
    assert test.rules_grid[0][1][0] == 0
    assert test.rules_grid[1][0][0] == 1
    assert test.rules_grid[1][1][0] == 0
    assert test.rules_grid[0][0][1] == 1 
    assert test.rules_grid[0][1][1] == 0
    assert test.rules_grid[1][0][1] == 0
    assert test.rules_grid[1][1][1] == 0