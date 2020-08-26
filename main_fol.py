from fol_formula import *
from term import *


term1 = Con('a')
term2 = Var('y')
term3 = Var('x')

term4 = Fun('f', [term3, term1])
term5 = Fun('g', [term4])
print(term4)
print(term5)

formula1 = Atom('P', [Con('a'), Var('x'), Fun('f', [Con('b'), Var('y')])])
print(formula1)

formula2 = Atom('R', [Fun('f', [Fun('g', [Con('b')]), Var('y')])])
print(formula2)

formula3 = ForAll(Var('x'), Implies(And(formula1, formula2), formula1))
print(formula3)

