"""
Module concerning Curator objects
"""

# Python Libraries
import numpy as np

# First Party Imports

class Curator:
    '''
    This is the director class that interacts with the
    Space, Painting and Rule classes.  Coordinates the checking
    of space-painting permutations against the rules listed.
    Provides the interface necessary for the user to narrow down
    options.
    '''
    # TODO: make default args using factories
    def __init__(
        self,
        rules,
        spaces,
        paintings
        ):
        self.rules = rules
        self.spaces = spaces
        self.paintings = paintings
        self.rules_grid = np.zeros((len(spaces), len(paintings), len(rules)))
        self.possibles = np.zeros((len(spaces), len(paintings)))

    def _update_rule_grid(self):
        '''
        Method that updates the rules tensor.
        Each rule has its own s x p two dimensional array.
        This method iterates and updates each of these
        two dimensional arrays.
        '''
        for r, rule in enumerate(self.rules):
            for s, space in enumerate(self.spaces):
                for p, painting in enumerate(self.paintings):
                    self.rules_grid[s][p][r] = rule.rule(space, painting)

    def hang_painting(self, space, painting):
        # set space.complete to 1
        # set painting.complete to 1
        # run update_rules_grid
        # 
        pass

    def return_fewest_options(self, n=3):
        pass
    # method return n fewest options


