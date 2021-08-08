"""
Module concerning Rule objects
"""

# Python Libraries
from abc import ABC, abstractmethod
from typing import Union
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
    grid: np.array
        The n x m array that holds all valid options
    '''
    def __init__(
        self,
        spaces: Union[list, tuple] = (),
        paintings: Union[list, tuple] = (),
        ):
        self.spaces = {i:space for i,space in enumerate(spaces) if spaces}
        self.paintings = {i:space for i,space in enumerate(paintings) if paintings}
        self.num_spaces = len(spaces)
        self.num_paintings = len(paintings)
        self.grid = np.zeros((len(spaces), len(paintings)))

    @abstractmethod
    def rule(self, space, painting):
        pass

    def update_grid(self):
        ''' 
        Method that iterates over each cell in the grid,
        checking if the pairing matches the rule.
        '''
        for i, space in enumerate(self.grid):
            for j, painting in enumerate(space):
                self.grid[i][j] = self.rule(self.spaces[i], self.paintings[j])

class HorizontalDimRule(Rule):
    '''
    This Rule checks whether the candidate painting fits the horizontal
    space available.
    Spaces that can hold multiple pieces are not subject to the minimum.
    '''
    def rule(self, space, painting):
        if space.max_pieces == 1:
            return space.min_hor_dim <= painting.horizontal_dim <= space.max_hor_dim
        else:
            return painting.horizontal_dim <= space.max_hor_dim

class VerticalDimRule(Rule):
    '''
    This Rule checks whether the candidate painting fits the vertical
    space available.
    Spaces that can hold multiple pieces are not subject to the minimum.
    '''
    def rule(self, space, painting):
        if space.max_pieces == 1:
            return space.min_ver_dim <= painting.vertical_dim <= space.max_ver_dim
        else:
            return painting.vertical_dim <= space.max_hor_dim            

class IndigenousPopArtRule(Rule):
    '''
    This Rule prevents a Pop Art painting and an Indigenous painting
    being hung on the same surface as it would lead to a clash
    of styles and an unwelcome aesthetic.
    '''
    def rule(self, space, painting):
        if space.categories:
            if 'indigenous' in ''.join(space.categories) and painting.category == 'pop art':
                return False
            if 'pop art' in ''.join(space.categories) and painting.category == 'indigenous':
                return False
        return True


class PosterRule(Rule):
    '''
    This Rule prevents more than one poster style painting
    being hung on the same surface
    '''
    def rule(self, space, painting):
        return not (painting.poster and space.contains_poster_flag)


class ColourClashRule(Rule):
    '''
    This Rule prevents paintings with clashing colour schemes
    from being hung on the same space.
    '''
    def __init__(
        self,
        spaces: Union[list, tuple] = (),
        paintings: Union[list, tuple] = (),
        ):
        super().__init__(spaces, paintings)
        self.colour_clash = {
            "red": "green",
            "black": "red",
            "green": "orange",
            "orange": "black",
            "yellow": "red",
        }
        self.colour_clash_rev = {v: k for k,v in self.colour_clash.items()}
    
    def rule(self, space, painting):
        if space.colours:
            for painting_colour in painting.colours:
                if painting_colour in self.colour_clash.keys() and \
                    self.colour_clash[painting_colour] in space.colours:
                    return False
                if painting_colour in self.colour_clash_rev.keys() and \
                    self.colour_clash_rev[painting_colour] in space.colours:
                    return False
        return True


class PrimeMatchRule(Rule):
    '''
    This Rule prevents a non-prime painting from being hung on a prime
    space
    '''
    def rule(self, space, painting):
        return (painting.prime_flag and space.prime_flag)


class MaxPiecesRule(Rule):
    '''
    This rule prevents a space that is at capacity from accepting an
    additional painting.
    '''
    def rule(self, space, painting):
        if space.paintings_hung:
            return not len(space.paintings_hung) == space.max_pieces
        else:
            return True

class SpaceCompleteRule(Rule):
    '''
    This Rule checks whether the space already is complete.
    ''' 
    def rule(self, space, painting):
        return not space.complete


class PaintingCompleteRule(Rule):
    '''
    This Rule checks whether the candidate painting is already
    hung on a space
    ''' 
    def rule(self, space, painting):
        return not painting.complete


class ContemporaryMasterRule(Rule):
    '''
    This Rule checks whether the candidate painting is hung next
    to a master of the same category.
    ''' 
    def rule(self, space, painting):
        if space.categories:
            if 'contemporary' in painting.category and 'master' in ' '.join(space.categories):
                return False
            elif 'master' in painting.category and 'contemporary' in ' '.join(space.categories):
                return False
        return True

# TODO: proportional rule