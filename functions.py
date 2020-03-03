"""The goal in this module is to define functions that take a formula as input and
do some computation on its syntactic structure. """


from formula import *


def length(formula):
    """Determines the length of a formula in propositional logic."""
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return length(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return length(formula.left) + length(formula.right) + 1


def subformulas(formula):
    """Removes the repetitions included by the function subformulas_aux."""
    subs = subformulas_aux(formula)
    result = []
    for sub in subs:
        included = False
        for sub2 in result:
            if sub == sub2:
                included = True
        if not included:
            result = result + [sub]
    return result


def subformulas_aux(formula):
    """Returns the set of all subformulas of a formula.
    It includes repetitions since x and y are distinct objects in the following code:
    x = Atom('p')
    y = Atom('p')"""

    if isinstance(formula, Atom):
        return [formula]
    if isinstance(formula, Not):
        return [formula] + subformulas_aux(formula.inner)
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        sub1 = subformulas_aux(formula.left)
        sub2 = subformulas_aux(formula.right)
        return [formula] + sub1 + sub2

#  we have shown in class that for all formula A, len(subformulas(A)) <= length(A).


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
