from interpretation_fol import *
from fol_functions import length_fol, variables_from_term

term1 = Con('a')
term2 = Var('y')
term3 = Var('x')
print(term1)
print(term2)

term4 = Fun('f', [term3, term1])
term5 = Fun('g', [term4])
print(term4)
print(term5)

print(f'Variables from {term1}: {variables_from_term(term1)}')
print(f'Variables from {term2}:')
for var in variables_from_term(term2):
    print(var)

print(f'Variables from {term4}:')
for var in variables_from_term(term4):
    print(var)

print(f'Variables from {term5}:')
for var in variables_from_term(term5):
    print(var)

formula1 = Atom('P', [Con('a'), Var('x'), Fun('f', [Con('b'), Var('y')])])
print(formula1)

formula2 = Atom('R', [Fun('f', [Fun('g', [Con('b')]), Var('y')])])
print(formula2)

formula3 = ForAll(Var('x'), Implies(And(formula1, formula2), formula1))
print(formula3)

formula4 = Or(Exists(Var('y'), And(formula1, formula2)), ForAll(Var('x'), formula2))
print(formula4)

print(f'length of {formula2} is {length_fol(formula2)}.')
print(f'length of {formula3} is {length_fol(formula3)}.')
print(f'length of {formula4} is {length_fol(formula4)}.')

interpretation1 = Interpretation(domain={1, 2, 3},
                                 predicates={'P': {(1, 1, 1), (2, 3, 1), (3, 1, 2), (3, 3, 2)},
                                             'R': {(1, 2), (2, 1), (2, 2), (2, 3), (3, 3)}},
                                 functions={
                                     'f': {(1, 1): 1, (1, 2): 2, (1, 3): 1, (2, 1): 1, (2, 2): 3, (2, 3): 2, (3, 1): 1,
                                           (3, 2): 2, (3, 3): 3},
                                     'g': {(1,): 2, (2,): 3, (3,): 2}},
                                 constants={'a': 1, 'b': 3},
                                 variables={'x': 2, 'y': 1}
                                 )

print(f'Domain: {interpretation1.domain}')
print(f'Interpretation of constant {term1.name} in interpretation1 is {interpretation1.constants[term1.name]}')
print(f'Interpretation of variable {term3.name} in interpretation1 is {interpretation1.variables[term3.name]}')
print(f'Interpretation of function {term4.name} in interpretation1 is {interpretation1.functions[term4.name]}')
print(f'Interpretation of predicate {formula1.name} in interpretation1 is {interpretation1.predicates[formula1.name]}')

# print(interpretation1.interpretation_term(term5))
# print(interpretation1.truth_value(formula3))
