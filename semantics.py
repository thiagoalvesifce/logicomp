"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """


from formula import *


def truth_value(formula, valuation):
    """Determines the truth value of a formula in a valuation.
    A valuation may be defined as dictionary. For example, {'p': True, 'q': False}.
    """
    pass
    # ======== YOUR CODE HERE ========


def logical_consequence(premises, conclusion):
    """Returns True if the conclusion is a logical consequence of the set of premises. Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========


def logical_equivalence(formula1, formula2):
    """Checks whether formula1 and formula2 are logically equivalent."""
    pass
    # ======== YOUR CODE HERE ========


def is_valid(formula):
    """Returns True if formula is a logically valid (tautology). Otherwise, it returns False"""
    pass
    # ======== YOUR CODE HERE ========


def is_satisfiable(formula):
    """Checks whether formula is satisfiable."""
    pass
    # ======== YOUR CODE HERE ========
