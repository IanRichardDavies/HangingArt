"""
Module concerning Rule objects
"""

# Python Libraries
from abc import ABC
import numpy as np

# First Party Imports

class Rule(ABC):
    '''
    An Abstract Base Class from which all concrete Rule classes will inherit.

    A n x m matrix where n is the number of spaces and m is the number of paintings
    Each cell contains a 1/0 indicating whether the potential match is allowed.
    Each rule object only compares one Space field to one Painting field.
    
    Parameters
    ----------
    spaces: dict
        A dict containing all Space objects under consideration.
        The key is the index (int) and value is a Space object
    paintings: dict
        The dict containing all Painting objects under consideration.
        The key is the index (int) and value is a Painting object
    num_spaces: int
        "n" the number of individual spaces available to hang paintings
    num_paintings: int
        "m" the number of individual paintings to be hung.
    space_field: str
        The Space object field to be used to check for a valid match
    painting_field: str
        The painting object field to be used to check for a valid match
    grid: np.array
        The n x m array that holds all valid options
    '''
    def __init__(
        self,
        spaces: list,
        paintings: list,
        space_field: str,
        painting_field: str,
        ):
        self.spaces = {i:space for i,space in enumerate(spaces,1)}
        self.paintings = {i:space for i,space in enumerate(paintings,1)}
        self.space_field = space_field
        self.painting_field = painting_field
        self.num_spaces = len(spaces)
        self.num_paintings = len(paintings)
        self.grid = np.zeroes((len(spaces), len(paintings)))

    @abstractmethod
    def rule(self, space, painting):
        pass

    def update_grid(self):
        ''' 
        Method that iterates over each cell in the grid,
        checking if the pairing matches the rule.

        '''
        for i, space in enumerate(self.grid,1):
            for j, painting in enumerate(space,1):
                space = self.spaces[i]
                painting = self.spaces[j]
                self.grid[i][j] = self.rule(space, painting)


class VertDimRule(Rule):
    pass



