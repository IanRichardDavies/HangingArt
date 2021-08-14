'''
Fixtures for pytest
'''

# Python Libraries
import pytest

# First Party Imports
import hangingart.rule as rule
from hangingart.painting import Painting
from hangingart.space import Space


@pytest.fixture(autouse=True)
def gen_paintings():
    painting_params = [
    ('Several Circles',30,30,'pop art',1,1,['black','purple','blue',],),
    ('Transformation',50,70,'indigenous',1,1,['orange','brown','blue',],),
    ]
    return [Painting(*param) for param in painting_params]


@pytest.fixture(autouse=True)
def gen_spaces():
    space_params = [
    (40,20,40,20,'kitchen','S','1', 1, 1,),
    (30,15,20,15,'kitchen','W','1', 1, 1,),
    ]
    return [Space(*param) for param in space_params]


@pytest.fixture(autouse=True)
def gen_rules():
    return [
        rule.HorizontalDimRule(),
        rule.VerticalDimRule(),
    ]
