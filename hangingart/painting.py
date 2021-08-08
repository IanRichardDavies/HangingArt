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
        name: str = '',
        horizontal_dim: float = 0.0,
        vertical_dim: float = 0.0, 
        category: str = '',
        poster: int = 0,
        prime_flag: int = 1,
        colours: list = None,
        complete: int = 0,
        ):
        self.name = name
        self.horizontal_dim = horizontal_dim
        self.vertical_dim = vertical_dim
        self.category = category
        self.poster = poster
        self.prime_flag = prime_flag
        self.colours = colours
        self.complete = complete

    def hang(self):
        '''
        Method that updates painting attributes after it
        is hung on a space.
        '''
        self.complete = 1

    def display(self):
        '''
        Method to display space attributes to user.
        '''
        # TODO: test
        if self.complete:
            complete_str = 'Y'
        else:
            complete_str = 'N'
        print(
            f"""
            Name: {self.name}
            Category: {self.category}
            Complete: {complete_str} 
            """
            )