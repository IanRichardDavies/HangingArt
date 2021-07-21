"""
Spaces object Factory.

Interface to create and access Space objects defined in space.py
"""

# Python Libraries

# First Party Imports
from hangingart.space import Space

"""
Order or parameters:
    horizontal_dim
    vertical_dim
    room
    surface_dir
    floor
    prime_flat
    max_pieces
"""

params = [
    (40,40,'kitchen','S','1', 1, 1,),
    (30,30,'kitchen','W','1', 1, 1,),

]

def generate_spaces(params):
    return [Space(*param) for param in params]