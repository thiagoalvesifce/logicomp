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
formula8 = Implies(Not(And(Atom('p'), Atom('s'))), And(Atom('q'), Not(And(Atom('p'), Atom('s')))))


print('formula1:', formula1)
print('formula2:', formula2)
print('formula3:', formula3)
print('formula4:', formula4)
print('formula5:', formula5)
print('formula6:', formula6)
print('formula7:', formula7)
print('formula8:', formula8)

print('length of formula1:', length(formula1))
print('length of formula3:', length(formula3))

print('length of formula7:', length(formula7))

print('subformulas of formula7:')
for subformula in subformulas(formula7):
    print(subformula)

print('length of formula8:', length(formula8))
print('subformulas of formula8:')
for subformula in subformulas(formula8):
    print(subformula)

#  we have shown in class that for all formula A, len(subformulas(A)) <= length(A):
# for example, for formula8:
print('number of subformulas of formula8:', len(subformulas(formula8)))
print('len(subformulas(formula8)) <= length(formula8):', len(subformulas(formula8)) <= length(formula8))
