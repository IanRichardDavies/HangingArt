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
        max_hor_dim: float = 0.0, 
        min_hor_dim: float = 0.0,
        max_ver_dim: float = 0.0, 
        min_ver_dim: float = 0.0, 
        room: str = '',
        surface_dir: str = '', 
        floor: int = 1,
        prime_flag: int = 1,
        max_pieces: int = 1,
        categories: list = None,
        complete: int = 0,
        contains_poster_flag: int = 0,
        colours: list = None,
        paintings_hung: list = None,
        margin: int = 6.0
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
        self.categories = categories
        self.name = f"{room} {surface_dir}"
        self.complete = complete
        self.contains_poster_flag = contains_poster_flag
        self.colours = colours
        self.paintings_hung = paintings_hung
        self.margin = margin

    def hang(self, painting):
        '''
        Method that updates the Space object attributes
        after a painting is hung.
        '''
        if self.paintings_hung:
            self.paintings_hung.append(painting)
        else:
            self.paintings_hung = [painting]
        if len(self.paintings_hung) == self.max_pieces:
            self.complete = 1
        self.max_ver_dim -= (painting.vertical_dim + self.margin)
        self.max_hor_dim -= (painting.horizontal_dim + self.margin)
        if self.categories:
            self.categories.append(painting.category)
        else:
            self.categories = [painting.category]
        if painting.poster:
            self.contains_poster_flag = 1
        if self.colours:
            self.colours.extend(painting.colours)
        else:
            self.colours = [painting.colours]
        # TODO: better documentation

    def display(self):
        '''
        Method to display space attributes to user.
        '''
        if self.complete:
            complete_str = 'Y'
        else:
            complete_str = 'N'
        print(
            f"""
            {self.room} {self.surface_dir}
            complete: {complete_str}
            Paintings hung:"""
            )
        if self.paintings_hung:
            for painting in self.paintings_hung:
                painting.display()