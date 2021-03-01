from fol_formula import *
from term import *


def length_fol(formula):
    """Determines the length of a formula in first-order logic."""
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return length_fol(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return length_fol(formula.left) + length_fol(formula.right) + 1
    if isinstance(formula, ForAll) or isinstance(formula, Exists):
        return 1 + length_fol(formula.inner)


def subformulas_fol(formula):
    """Returns the set of all subformulas of a first-order formula"""
    pass


def constants_from_term(term):
    """Returns the set of all constant occurring in a term"""
    pass


def variables_from_term(term):
    """Returns the set of all variables occurring in a term"""
    if isinstance(term, Con):
        return set()
    if isinstance(term, Var):
        return {term}
    if isinstance(term, Fun):
        variables = set()
        for inner_term in term.args:
            variables = variables.union(variables_from_term(inner_term))
        return variables


def function_symbols_from_term(term):
    """Returns the set of all function symbols occurring in a term
    For example, function_symbols_from_term(Fun('f', [Var('x'), Con('a')]))
    must return {'f'}

    and

    function_symbols_from_term(Fun('g', [Fun('f', [Var('x'), Con('a')])]))
    must return {'f', 'g'}
    """
    pass


def all_constants(formula):
    """Returns the set of all constant occurring in a formula"""
    pass


def predicate_symbols(formula):
    """Returns the set of all predicate symbols occurring in a formula.
    For example, predicate_symbols(Or(Atom('P', [Con('a')]), Atom('R', [Var('x')])))
    must return {'P', 'R'}
    """
    pass


def function_symbols(formula):
    """Returns the set of all function symbols occurring in a formula.
    For example, predicate_symbols(Or(Atom('P', [Fun('f', [Con('b'), Var('y')])]),
                                      Atom('P', [Fun('g', [Var('y')])])
                                      )
                                   )
    must return {'f', 'g'}
    """
    pass


def atoms_fol(formula):
    """Returns the set of all atomic suformulas of a first-order formula"""
    pass


def free_variables(formula):
    """Returns the set of all free variables of a formula"""
    pass


def bounded_variables(formula):
    """Returns the set of all bounded variables of a formula"""
    pass


def universal_closure(formula):
    """Returns the universal closure of a formula"""
    pass


def existential_closure(formula):
    """Returns the existential closure of a formula"""
    pass


def number_free_occurrences(var, formula):
    """Returns the number of free occurrences of variable var in formula.
    For example, number_free_occurrences(Var('x'),
                                         ForAll(Var('y'), Implies(And(Atom('P', [Var('x')]),
                                                                      Atom('Q', [Var('y')])),
                                                                  ForAll(Var('x'), Atom('Q', [Var('x')]))
                                                                 )
                                               )
                                        )
    must return 1
    """
    pass


# scope?
# quantifier-free
# closed term / ground terms
# closed formula / sentence
