"""Se João ganhar as eleições, a criminalidade aumentará se a escolaridade não melhorar."""

from semantics import *

ganhar = Atom('joão ganha a eleição')
mais_escolaridade = Atom('a escolaridade melhora')
mais_crimes = Atom('criminalidade aumenta')

formula1 = Implies(ganhar, Implies(Not(mais_escolaridade), mais_crimes))

formula2 = Implies(And(ganhar, Not(mais_escolaridade)), mais_crimes)

print(is_logical_equivalence(formula1, formula2))
