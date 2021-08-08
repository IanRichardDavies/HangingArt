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
# TODO: review values
@pytest.fixture
def gen_paintings():
    painting_params = [
    ('Several Circles',30,30,'pop art',1,1,['black','purple','blue',],),
    ('Transformation',50,70,'indigenous',1,1,['orange','brown','blue',],),
    ]
    return [Painting(*param) for param in painting_params]

#TODO: create and move to conftest.py
#TODO: update values
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


def test_IndPop_rule(gen_spaces, gen_paintings):
    gen_spaces[0].categories = ['pop art']
    gen_spaces[1].categories = ['indigenous']
    # remove any dimensional constraints
    gen_paintings[0].horizontal_dim = 25.0
    gen_paintings[0].horizontal_dim = 25.0
    gen_paintings[1].vertical_dim = 25.0
    gen_paintings[1].vertical_dim = 25.0
    test = rule.IndigenousPopArtRule(gen_spaces, gen_paintings)
    test.update_grid()
    assert test.grid[0][0] == 1 
    assert test.grid[0][1] == 0
    assert test.grid[1][0] == 0
    assert test.grid[1][1] == 1


def test_painting_complete_rule(gen_spaces):
    painting = Painting('test', 10, 10, 'category', 1, 1, ['blue'], 1)
    test = rule.PaintingCompleteRule(gen_spaces, [painting])
    test.update_grid()
    assert test.grid[0][0] == 0
    assert test.grid[1][0] == 0

def test_space_complete_rule(gen_paintings):
    space = Space(
        'test', 
        100, 
        10,
        50,
        5,
        'kitchen',
        'N',
        '1',
        1,
        complete = 1)
    test = rule.SpaceCompleteRule([space], gen_paintings)
    test.update_grid()
    assert test.grid[0][0] == 0
    assert test.grid[0][1] == 0


def test_has_poster_rule(gen_paintings):
    space = Space(
        'test', 
        100, 
        10,
        50,
        5,
        'kitchen',
        'N',
        '1',
        1,
        contains_poster_flag = 1)
    test = rule.PosterRule([space], gen_paintings)
    test.update_grid()
    assert test.grid[0][0] == 0
    assert test.grid[0][1] == 0


def test_colourclash_rule(gen_paintings):
    space = Space(
        'test', 
        100, 
        10,
        50,
        5,
        'kitchen',
        'N',
        '1',
        1,
        colours = ['red'])
    test = rule.ColourClashRule([space], gen_paintings)
    test.update_grid()
    assert test.grid[0][0] == 0 
    assert test.grid[0][1] == 1


def test_primematch_rule(gen_spaces, gen_paintings):
    gen_paintings[0].prime_flag = 0
    test = rule.PrimeMatchRule(gen_spaces, gen_paintings)
    test.update_grid()
    assert test.grid[0][0] == 0 
    assert test.grid[0][1] == 1
    assert test.grid[1][0] == 0
    assert test.grid[1][1] == 1


def test_maxpieces_rule(gen_paintings):
    space = Space(
        'test', 
        100, 
        10,
        50,
        5,
        'kitchen',
        'N',
        '1',
        1,
        )
    painting = Painting('test', 10, 10, 'category', 1, 1, ['blue'], 1)
    space.paintings_hung = [painting]
    test = rule.MaxPiecesRule([space], gen_paintings)
    test.update_grid()
    assert test.grid[0][0] == 0 
    assert test.grid[0][1] == 0


def test_contemporary_master_rule(gen_spaces, gen_paintings):
    gen_spaces[0].categories = ['master genre']
    gen_paintings[0].category = 'master genre'
    gen_spaces[1].categories = ['contemporary category']
    gen_paintings[1].category = 'contemporary category'
    test = rule.ContemporaryMasterRule(gen_spaces, gen_paintings)
    test.update_grid()
    print(test.grid)
    assert test.grid[0][0] == 1 
    assert test.grid[0][1] == 0
    assert test.grid[1][0] == 0
    assert test.grid[1][1] == 1