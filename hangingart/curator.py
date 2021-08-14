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
        for space in self.spaces:
            space.display()

    def display_paintings(self):
        '''
        Interface to the display method of Painting objects.
        '''
        for painting in self.paintings:
            painting.display()

    def _match_space(self, description: str) -> int:
        '''
        Method that returns the Space object that matches a user's string arg.
        Example call: 
        curator._match_space('kitchen N')

        Paramters
        ---------
        description: str
            A description of the space

        Returns
        -------
        The index of the matching Space object
        '''
        for i, space in enumerate(self.spaces):
            if description.split()[0] in space.room and \
                space.surface_dir == description.split()[-1]:
                return i
        print ("No such space found.")
        return -1

    def _match_painting(self, description: str) -> int:
        '''
        Method that returns the Painting object that matches a user's string arg.
        Example call: 
        curator._match_painting('Several circles')

        Paramters
        ---------
        description: str
            A description of the painting.

        Returns
        -------
        The index of the matching Painting object
        '''
        for i, painting in enumerate(self.paintings):
            if description.lower() in painting.name.lower():
                return i
        print ("No such painting found.")
        return -1

    def hang_painting(self, space_str: str, painting_str: str):
        '''
        Method that confirms a space-painting pairing.

        '''
        s_idx = self._match_space(space_str)
        p_idx = self._match_painting(painting_str)
        self.spaces[s_idx].hang(self.paintings[p_idx])
        self.paintings[p_idx].hang()
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

    def options_available(self, description: str):
        '''
        Method that prints out the options available for a specific space
        '''
        self._update_rule_grid()
        self.possibles = np.prod(self.rules_grid, axis=0)
        self.space_sums = np.sum(self.possibles, axis=1)
        idx = self._match_space(description)
        painting_indices = self.possibles[idx]
        for i, boolean in enumerate(painting_indices):
            if boolean:
                print(self.paintings[i].name)

    def display_this_space(self, description: str) -> None:
        '''
        Method that displays the information for a specific Space object.

        Paramters
        ---------
        description: str
            A description of the space
        '''
        idx = self._match_space(description)
        self.spaces[idx].display()

    def display_this_painting(self, description: str) -> None:
        '''
        Method that displays the information for a specific Painting object.

        Paramters
        ---------
        description: str
            A description of the painting
        '''
        idx = self._match_painting(description)
        self.paintings[idx].display()
