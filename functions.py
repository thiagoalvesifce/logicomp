"""The goal in this module is to define functions that take a formula as input and
do some computation on its syntactic structure. """


from formula import *


def length(formula):
    """Determines the length of a formula in propositional logic."""
    if isinstance(formula, Atom):
        return 1
    # ======== YOUR CODE HERE ========


def subformulas(formula):
    """Returns the set of all subformulas of a formula."""
    pass
    # ======== YOUR CODE HERE ========


def atoms(formula):
    """Returns the set of all atoms occurring in a formula."""
    pass
    # ======== YOUR CODE HERE ========


def number_of_atoms(formula):
    """Returns the number of distinct atoms occurring in a formula."""
    pass
    # ======== YOUR CODE HERE ========


def number_of_connectives(formula):
    """Returns the number of connectives occurring in a formula."""
    pass
    # ======== YOUR CODE HERE ========


def substitution(formula, old_subformula, new_subformula):
    """Returns a new formula obtained by replacing all occurrences
    of old_subformula in the input formula by new_subformula."""
    pass
    # ======== YOUR CODE HERE ========
