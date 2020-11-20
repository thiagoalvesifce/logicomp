from interpretation_fol import *

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

formula4 = Or(Exists(Var('y'), And(formula1, formula2)), ForAll(Var('x'), formula2))
print(formula4)

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

print(interpretation1.domain)
print(term1.name, interpretation1.constants[term1.name])
print(term3.name, interpretation1.variables[term3.name])
print(term4.name, interpretation1.functions[term4.name])
print(formula1.name, interpretation1.predicates[formula1.name])

# print(interpretation1.truth_value(formula3))
