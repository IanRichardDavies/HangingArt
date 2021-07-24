"""
Module concerning Painting objects
"""

# Python Libraries

# First Party Imports

class Painting:
    """
    Class holding logic for each individual piece of art
    """
    def __init__(
        self,
        name,
        horizontal_dim: float,
        vertical_dim: float, 
        category: str,
        poster: int,
        prime_flag: int,
        colours: list,
        complete: int = 0,
        possible_spaces: list = None,
        disallowed_space: list = None,
        ):
        self.name = name
        self.horizontal_dim = horizontal_dim
        self.vertical_dim = vertical_dim
        self.category = category
        self.poster = poster
        self.prime_flag = prime_flag
        self.colours = colours
        self.complete = complete
        self.possible_spaces = possible_spaces
        self.disallowed_space = disallowed_space

