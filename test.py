"""You can test your functions in this module as in the following code: """


from formula import *
from functions import *


formula1 = Atom('p')
formula2 = Atom('q')
formula3 = And(formula1, formula2)
formula4 = And(Atom('p'), Atom('s'))
formula5 = Not(And(Atom('p'), Atom('s')))
formula6 = Or(Not(And(Atom('p'), Atom('s'))), Atom('q'))
formula7 = Implies(Not(And(Atom('p'), Atom('s'))), And(Atom('q'), Atom('r')))

print(formula1)
print(formula2)
print(formula3)
print(formula4)
print(formula5)
print(formula6)
print(formula7)

print(length(formula1))
print(length(formula3))
