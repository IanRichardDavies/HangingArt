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
        prime_flag: int,
        possible_spaces: list = None,
        disallowed_space: list = None,
        ):
        self.name = name
        self.horizontal_dim = horizontal_dim
        self.vertical_dim = vertical_dim
        self.category = category
        self.prime_flag = prime_flag
        self.possible_spaces = possible_spaces
        self.disallowed_space = disallowed_space

