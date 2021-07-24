"""
Spaces object Factory.

Interface to create and access Space objects defined in space.py
"""

# Python Libraries

# First Party Imports
from hangingart.space import Space

"""
Order or parameters:
    max_horizontal_dim
    min_horizontal_dim
    max_vertical_dim
    min_vertical_dim
    room
    surface_dir
    floor
    prime_flat
    max_pieces
"""

params = [
    (40,20,40,20,'kitchen','S','1', 1, 1,),
    (30,15,30,15,'kitchen','W','1', 1, 1,),

]

def generate_spaces(params):
    return [Space(*param) for param in params]