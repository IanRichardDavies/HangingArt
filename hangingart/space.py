"""
Module concerning Space objects
"""

# Python Libraries

# First Party Imports

class Space:
    """
    Class holding logic for each individual surface
    upon which art can be hung.
    #TODO: more documentation
    """
    def __init__(
        self,
        max_hor_dim: float, 
        min_hor_dim: float,
        max_ver_dim: float, 
        min_ver_dim: float, 
        room: str,
        surface_dir: str, 
        floor: str,
        prime_flag: int,
        max_pieces: int = 1,
        possible_paintings: list = None,
        disallowed_paintings: list = None,
        categories: list = None,
        disallowed_categories: list = None,
        complete: int = 0,
        contains_poster_flag: int = 0,
        colours: list = None,
        paintings_hung: list = None,
        ): 
        self.max_hor_dim = max_hor_dim
        self.min_hor_dim = min_hor_dim
        self.max_ver_dim = max_ver_dim
        self.min_ver_dim = min_ver_dim
        self.room = room
        self.surface_dir = surface_dir
        self.floor = floor
        self.prime_flag = prime_flag
        self.max_pieces = max_pieces
        self.possible_paintings = possible_paintings
        self.disallowed_paintings = disallowed_paintings # necessary
        self.categories = categories
        self.disallowed_categories = disallowed_categories # necessary?
        self.name = f"{room} {surface_dir}"
        self.complete = complete
        self.contains_poster_flag = contains_poster_flag
        self.colours = colours
        self.paintings_hung = paintings_hung

        #TODO: margin attribute
        #TODO: hang painting method
        #TODO: have dimensions updated after painting is hung
        #TODO: have categories updated after painting is hung
        #TODO: have colours updated after painting is hung