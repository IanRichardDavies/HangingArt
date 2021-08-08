"""
Spaces object Factory.

Interface to create and access Space objects defined in space.py
"""

# Python Libraries

# First Party Imports
from hangingart.space import Space


PARAMS = [
    {
        'max_hor_dim': 33.0, 
        'min_hor_dim': 16.0 ,
        'max_ver_dim': 30.0, 
        'min_ver_dim': 16.0, 
        'room': 'kitchen',
        'surface_dir': 'S', 
        'floor': 1,
        'prime_flag': 1,
        'max_pieces': 1,
    },
    {
        'max_hor_dim': 28.0, 
        'min_hor_dim': 14.0 ,
        'max_ver_dim': 40.0, 
        'min_ver_dim': 10.0, 
        'room': 'kitchen',
        'surface_dir': 'W', 
        'floor': 1,
        'prime_flag': 1,
        'max_pieces': 1,
    },
    {
        'max_hor_dim': 41.0, 
        'min_hor_dim': 16.0 ,
        'max_ver_dim': 30.0, 
        'min_ver_dim': 15.0, 
        'room': 'dining room',
        'surface_dir': 'N', 
        'floor': 1,
        'prime_flag': 1,
        'max_pieces': 1,
    },
    {
        'max_hor_dim': 58.0, 
        'min_hor_dim': 20.0 ,
        'max_ver_dim': 38.0, 
        'min_ver_dim': 12.0, 
        'room': 'living room',
        'surface_dir': 'E', 
        'floor': 1,
        'prime_flag': 1,
        'max_pieces': 1,
    },
    {
        'max_hor_dim': 120.0, 
        'min_hor_dim': 60.0 ,
        'max_ver_dim': 58.0, 
        'min_ver_dim': 20.0, 
        'room': 'living room',
        'surface_dir': 'S', 
        'floor': 1,
        'prime_flag': 1,
        'max_pieces': 3,
    },
]

def generate_spaces():
    return [Space(**param) for param in PARAMS]