"""
Unit tests for curator module
"""

# Python Libraries
import numpy as np
import pytest

# First Party Imports
import hangingart.rule as rule
from hangingart.curator import Curator
from hangingart.painting import Painting
from hangingart.space import Space


def test_create_grid(gen_rules, gen_spaces, gen_paintings):
    test = Curator(gen_rules, gen_spaces, gen_paintings)
    assert test.rules_grid.shape == (2,2,2)


def test_update_rule_grid(gen_rules, gen_spaces, gen_paintings):
    test = Curator(gen_rules, gen_spaces, gen_paintings)
    test._update_rule_grid()
    assert test.rules_grid[0][0][0] == 1
    assert test.rules_grid[0][1][0] == 1
    assert test.rules_grid[1][0][0] == 1
    assert test.rules_grid[1][1][0] == 0
    assert test.rules_grid[0][0][1] == 0 
    assert test.rules_grid[0][1][1] == 0
    assert test.rules_grid[1][0][1] == 0
    assert test.rules_grid[1][1][1] == 0


def test_hang_painting(gen_rules, gen_spaces, gen_paintings):
    test = Curator(gen_rules, gen_spaces, gen_paintings)
    test.hang_painting('kitchen W', 'Transformation')
    assert test.rules_grid[0][0][0] == 1
    assert test.rules_grid[0][1][0] == 0
    assert test.rules_grid[1][0][0] == 1
    assert test.rules_grid[1][1][0] == 0
    assert test.rules_grid[0][0][1] == 0 
    assert test.rules_grid[0][1][1] == 0
    assert test.rules_grid[1][0][1] == 0
    assert test.rules_grid[1][1][1] == 0


def test_return_fewest(gen_rules, gen_spaces, gen_paintings):
    test = Curator(gen_rules, gen_spaces, gen_paintings) 
    test.hang_painting('kitchen W', 'Transformation')
    test._update_rule_grid()
    test.possibles = np.prod(test.rules_grid, axis=0)
    test.space_sums = np.sum(test.possibles, axis=0)
    test._space_with_fewest_options()
    assert test.min_space == gen_spaces[0]


def test_fewest_painting_options(
    gen_rules, 
    gen_spaces, 
    gen_paintings,
    capsys):
    test = Curator(gen_rules, gen_spaces, gen_paintings) 
    test.hang_painting('kitchen W', 'Transformation')
    test._update_rule_grid()
    test.possibles = np.prod(test.rules_grid, axis=0)
    test.space_sums = np.sum(test.possibles, axis=0)
    test._space_with_fewest_options()
    test._painting_options_for_min_space()
    captured = capsys.readouterr()
    assert 'Several Circles' in captured.out


def test_fewest_options(
    gen_rules, 
    gen_spaces, 
    gen_paintings,
    capsys):
    test = Curator(gen_rules, gen_spaces, gen_paintings) 
    test.hang_painting('kitchen W', 'Transformation')
    test.fewest_options()
    captured = capsys.readouterr()
    assert 'Several Circles' in captured.out
    assert 'kitchen' in captured.out
    assert 'S' in captured.out


def test_options_available(
    gen_rules, 
    gen_spaces, 
    gen_paintings,
    capsys):
    test = Curator(gen_rules, gen_spaces, gen_paintings) 
    test.hang_painting('kitchen W', 'Transformation')
    test.options_available('kitchen S')
    captured = capsys.readouterr()
    assert 'Several Circles' in captured.out


def test_display_space(
    gen_rules, 
    gen_spaces, 
    gen_paintings,
    capsys):
    test = Curator(gen_rules, gen_spaces, gen_paintings)
    test.display_this_space('kitchen S')
    captured = capsys.readouterr()
    assert 'kitchen S' in captured.out


def test_display_painting(
    gen_rules, 
    gen_spaces, 
    gen_paintings,
    capsys):
    test = Curator(gen_rules, gen_spaces, gen_paintings)
    test.display_this_painting('several circles')
    captured = capsys.readouterr()
    assert 'Several Circles' in captured.out
    assert 'pop art' in captured.out


def test_display_spaces(
    gen_rules, 
    gen_spaces, 
    gen_paintings,
    capsys):
    test = Curator(gen_rules, gen_spaces, gen_paintings)
    test.display_spaces()
    captured = capsys.readouterr()
    assert 'kitchen S' in captured.out
    assert 'kitchen W' in captured.out


def test_display_paintings(
    gen_rules, 
    gen_spaces, 
    gen_paintings,
    capsys):
    test = Curator(gen_rules, gen_spaces, gen_paintings)
    test.display_paintings()
    captured = capsys.readouterr()
    assert 'Transformation' in captured.out
    assert 'Several Circles' in captured.out


def test_match_space(
    gen_rules, 
    gen_spaces, 
    gen_paintings,):
    test = Curator(gen_rules, gen_spaces, gen_paintings)
    idx = test._match_space('kitchen W')
    assert idx == 1


def test_no_match_space(
    gen_rules, 
    gen_spaces, 
    gen_paintings,
    capsys):
    test = Curator(gen_rules, gen_spaces, gen_paintings)
    idx = test._match_space('bedroom N')
    captured = capsys.readouterr()
    assert 'No such space found.' in captured.out
    assert idx == -1


def test_match_painting(
    gen_rules, 
    gen_spaces, 
    gen_paintings,):
    test = Curator(gen_rules, gen_spaces, gen_paintings)
    idx = test._match_painting('Several Circles')
    assert idx == 0


def test_no_match_painting(
    gen_rules, 
    gen_spaces, 
    gen_paintings,
    capsys):
    test = Curator(gen_rules, gen_spaces, gen_paintings)
    idx = test._match_painting('Elegy to the Spanish Republic')
    captured = capsys.readouterr()
    assert 'No such painting found.' in captured.out
    assert idx == -1