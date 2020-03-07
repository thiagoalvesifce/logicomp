"""Considere que pessoas honestas sempre falam a verdade e pessoas mentirosas sempre mentem.
Além disso, suponha que toda pessoa é honesta ou mentirosa, mas não ambos.

Você conhece Amy e Bob.
Amy diz: “Bob e eu somos mentirosos.”

Qual a categoria de Amy e Bob?"""

from semantics import *

amy_honest = Atom('amy é honesta')
bob_honest = Atom('bob é honesto')

#  Amy diz que ambos são mentirosos.
#  Amy é honesta se e somente se o que ela diz é verdade
formula = And(Implies(amy_honest, And(Not(amy_honest), Not(bob_honest))),
              Implies(And(Not(amy_honest), Not(bob_honest)), amy_honest))


print(is_satisfiable(formula))
