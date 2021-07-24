"""
Rules object Factory.

Interface to create and access Rule objects defined in rule.py
"""

# Python Libraries

# First Party Imports
import hangingart.rule as rule


rules = [
    rule.HorizontalDimRule(),
    rule.VerticalDimRule(),
    rule.IndigenousPopRule(),
    rule.PosterRule(),
    rule.ColourClashRule(),
    rule.PrimeMatchRule(),
    rule.MaxPiecesRule(),
    rule.SpaceCompleteRule(),
    rule.PaintingCompleteRule(),
]
