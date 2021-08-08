"""
Module concerning Curator objects
"""

# Python Libraries
import copy
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
        self.rules_grid = np.zeros((len(rules), len(spaces), len(paintings)))
        self.possibles = np.zeros((len(spaces), len(paintings)))
        self.space_sums = np.zeros((len(spaces)))
        self.min_space = None
        self.min_space_idx = 0

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
                    self.rules_grid[r][s][p] = rule.rule(space, painting)

    def display_spaces(self):
        '''
        Interface to the display method of Space objects.
        '''
        # TODO: test
        for space in self.spaces:
            space.display()

    def display_paintings(self):
        '''
        Interface to the display method of Painting objects.
        '''
        # TODO: test
        for painting in self.painting:
            painting.display()

    def _match_space(self, description):
        pass

    def _match_painting(self, description):
        pass

    def hang_painting(self, space, painting):
        '''
        Method that confirms a space-painting pairing.

        '''
        #TODO: identify space and painting by names - new method
        space.hang(painting)
        painting.hang()
        self._update_rule_grid()

    def _space_with_fewest_options(self):
        '''
        Method that returns the space with the fewest possible options.
        '''
        if np.count_nonzero(self.space_sums):
            self.min_space_idx = np.argmin(self.space_sums[np.nonzero(self.space_sums)])
            self.min_space = self.spaces[self.min_space_idx]
            print(self.min_space.room, self.min_space.surface_dir)
        else:
            self.min_space = None
            print("No options available.")

    def _painting_options_for_min_space(self):
        '''
        Method that returns the space with the fewest possible options.
        '''
        if self.min_space:
            indices = self.possibles[self.min_space_idx]
            for i, boolean in enumerate(indices):
                if boolean:
                    print(self.paintings[i].name)

    def fewest_options(self):
        '''
        Method that calcualtes and prints out the space with the fewest
        options available, and what those paintings are.
        '''
        self._update_rule_grid()
        self.possibles = np.prod(self.rules_grid, axis=0)
        self.space_sums = np.sum(self.possibles, axis=1)
        self._space_with_fewest_options()
        self._painting_options_for_min_space()

    def options_available(self, room: str, surface_dir: str):
        '''
        Method that prints out the options available for a specific space
        '''
        self._update_rule_grid()
        self.possibles = np.prod(self.rules_grid, axis=0)
        self.space_sums = np.sum(self.possibles, axis=1)
        idx = -1
        for i, space in enumerate(self.spaces):
            if space.room == room and space.surface_dir == surface_dir:
                idx = i
                break
        if idx < 0:
            print ("No such space found.")
        painting_indices = self.possibles[idx]
        for i, boolean in enumerate(painting_indices):
            if boolean:
                print(self.paintings[i].name)
