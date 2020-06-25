"""Considere que pessoas honestas sempre falam a verdade e pessoas mentirosas sempre mentem.
Além disso, suponha que toda pessoa é honesta ou mentirosa, mas não ambos.

Você conhece Amy.
Amy diz: “Eu sou mentirosa.”

Essa situação é possível nas condições do puzzle?
É possível dizer a categoria de Amy? Justifique."""


from semantics import *

amy_honest = Atom('amy é honesta')

#  Amy diz que é mentirosa.
#  Amy é honesta se e somente se o que ela diz é verdade
formula = And(Implies(amy_honest, Not(amy_honest)),
              Implies(Not(amy_honest), amy_honest))


print(is_satisfiable(formula))
