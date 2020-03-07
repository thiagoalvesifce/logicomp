""" Did it rain yesterday?
Se choveu ontem, a rua ficou molhada.
A rua ficou molhada.
É possível concluir que choveu ontem?
"""

from formula import *
from semantics import *

rained = Atom('choveu ontem')
wet = Atom('a rua ficou molhada')

# Se choveu ontem, a rua ficou molhada.
premissa1 = Implies(rained, wet)

# A rua ficou molhada.
premissa2 = wet

# choveu ontem
conclusao = rained

print(premissa1)
print(premissa2)
print(conclusao, '?')

print(is_logical_consequence([premissa1, premissa2], conclusao))
