"""
Module concerning Space objects
"""

# Python Libraries

# First Party Imports

class Space():
    """
    Class holding logic for each individual surface
    upon which art can be hung.
    """
    def __init__(
        self,
        horizontal_dim: float,
        vertical_dim: float, 
        room: str,
        surface_dir: str, 
        floor: str,
        prime_flag: int,
        max_pieces: int = 1,
        possible_paintings: list = None,
        disallowed_paintings: list = None,
        categories: list = None,
        disallowed_categories: list = None,
        ):
        self.horizontal_dim = horizontal_dim
        self.vertical_dim = vertical_dim
        self.room = room
        self.surface_dir = surface_dir
        self.floor = floor
        self.prime_flag = prime_flag
        self.max_pieces = max_pieces
        self.possible_paintings = possible_paintings
        self.disallowed_paintings = disallowed_paintings
        self.categories = categories
        self.disallowed_categories = disallowed_categories
        self.name = f"{room} {surface_dir}"
