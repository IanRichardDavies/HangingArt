"""
Paintings object Factory.

Interface to create and access Painting objects defined in painting.py
"""

# Python Libraries

# First Party Imports


from hangingart.painting import Painting


PARAMS = [
    {
        'name': 'Robert Maplethorpe', 
        'horizontal_dim': 13.0,
        'vertical_dim': 11.0, 
        'category': 'photogaphy', 
        'poster': 0,
        'prime_flag': 0,
        'colours': ['black', 'white'],
    },
    {
        'name': 'Small block of spirals', 
        'horizontal_dim': 6.5,
        'vertical_dim': 5.5, 
        'category': 'abstract - contemporary', 
        'poster': 0,
        'prime_flag': 0,
        'colours': ['blue', 'orange'],
    },
    {
        'name': 'Naim Jain', 
        'horizontal_dim': 48.0,
        'vertical_dim': 24.0, 
        'category': 'abstract expressionism - contemporary', 
        'poster': 0,
        'prime_flag': 1,
        'colours': ['blue', 'green', 'purple',],
    },
    {
        'name': 'Greek postcards', 
        'horizontal_dim': 19.0,
        'vertical_dim': 8.5, 
        'category': 'pop art', 
        'poster': 0,
        'prime_flag': 0,
        'colours': ['blue', 'green', 'orange',],
    },
    {
        'name': 'Roy Lichtenstein', 
        'horizontal_dim': 21.5,
        'vertical_dim': 21.75, 
        'category': 'pop art', 
        'poster': 0,
        'prime_flag': 0,
        'colours': ['blue', 'black',],
    },
    {
        'name': 'Kandinsky', 
        'horizontal_dim': 16.0,
        'vertical_dim': 20.0, 
        'category': 'abstract expressionism - master', 
        'poster': 1,
        'prime_flag': 1,
        'colours': ['green', 'yellow', 'red',],
    },
    {
        'name': 'Skulls', 
        'horizontal_dim': 23.0,
        'vertical_dim': 19.0, 
        'category': 'pop art', 
        'poster': 0,
        'prime_flag': 0,
        'colours': ['black', 'white',],
    },
    {
        'name': 'Norval Morrisseau', 
        'horizontal_dim': 11.0,
        'vertical_dim': 13.5, 
        'category': 'indigenous', 
        'poster': 0,
        'prime_flag': 1,
        'colours': ['black', 'red', 'green',],
    },
    {
        'name': 'Saturn', 
        'horizontal_dim': 12.0,
        'vertical_dim': 15.0, 
        'category': 'drawing', 
        'poster': 0,
        'prime_flag': 0,
        'colours': ['black', 'red', 'white',],
    },
    {
        'name': 'Three women', 
        'horizontal_dim': 19.0,
        'vertical_dim': 8.5, 
        'category': 'indigenous', 
        'poster': 0,
        'prime_flag': 1,
        'colours': ['green', 'red', 'blue', 'orange',],
    },
    {
        'name': 'Simon Hantai', 
        'horizontal_dim': 23.0,
        'vertical_dim': 26.0, 
        'category': 'abstract expressionism	- master', 
        'poster': 0,
        'prime_flag': 1,
        'colours': ['blue', 'purple',],
    },
    {
        'name': 'Miro Dog', 
        'horizontal_dim': 15.5,
        'vertical_dim': 12.5, 
        'category': 'surrealism', 
        'poster': 0,
        'prime_flag': 1,
        'colours': ['brown', 'orange',],
    },
    {
        'name': 'Convergence', 
        'horizontal_dim': 42.0,
        'vertical_dim': 27.5, 
        'category': 'abstract expressionism - master', 
        'poster': 1,
        'prime_flag': 1,
        'colours': ['yellow', 'orange', 'black'],
    },
    {
        'name': 'Picasso', 
        'horizontal_dim': 14.0,
        'vertical_dim': 11.0, 
        'category': 'abstract - master', 
        'poster': 0,
        'prime_flag': 0,
        'colours': ['grey', 'black'],
    },
    {
        'name': 'Elegy to the Spanish Republic', 
        'horizontal_dim': 28.0,
        'vertical_dim': 22.0, 
        'category': 'abstract expressionism - master', 
        'poster': 0,
        'prime_flag': 1,
        'colours': ['black', 'blue', 'brown',],
    },
    {
        'name': 'Albers', 
        'horizontal_dim': 23.5,
        'vertical_dim': 27.0, 
        'category': 'abstract, suprematism - master', 
        'poster': 1,
        'prime_flag': 1,
        'colours': ['yellow', 'white',],
    },
    {
        'name': 'Woman by de Kooning', 
        'horizontal_dim': 16.0,
        'vertical_dim': 19.5, 
        'category': 'abstract expressionism - master', 
        'poster': 1,
        'prime_flag': 1,
        'colours': ['green', 'orange', 'pink',],
    },
    {
        'name': 'Small Jain', 
        'horizontal_dim': 12.5,
        'vertical_dim': 10.5, 
        'category': 'abstract expressionism - contemporary', 
        'poster': 0,
        'prime_flag': 1,
        'colours': ['green', 'yellow', 'red',],
    },
]

def generate_paintings():
    return [Painting(**param) for param in PARAMS]