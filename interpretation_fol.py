"""This module is designed to define interpretations for first-order logic.
For example, the following piece of code creates an object representing an interpretation for the formula
(∀x((P(a, x, f(b, y)) ∧ R(f(g(b), y))) ⟶ P(a, x, f(b, y)))).

interpretation1 = Interpretation(domain = {1, 2, 3},
                  predicates = {'P':{(1,1,1), (2,3,1), (3,1,2), (3,3,2)}
                                'R':{(1, 2), (2,1), (2,2), (2,3), (3,3)}},
                  functions = {'f':{(1,1):1, (1,2):2, (1,3):1, (2,1):1, (2,2):3, (2,3):2, (3,1):1, (3,2):2, (3,3):3},
                               'g':{(1): 2, (2): 3, (3): 2}},
                  constants = {'a': 1, 'b': 3},
                  variables = {'x' : 2, 'y': 1}
                  )
"""

from fol_formula import *
from term import *


class Interpretation:
    def __init__(self, domain, predicates, functions, constants, variables):
        self.domain = domain
        self.predicates = predicates
        self. functions = functions
        self.constants = constants
        self.variables = variables

    def truth_value(self, formula):
        pass
