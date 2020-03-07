""" Bus in the station
Se o trem chegou tarde e não tinha ônibus na estação, então João chegou atrasado para a reunião.
João não chegou atrasado para a reunião.
O trem chegou tarde na estação.
É possível concluir que tinha ônibus na estação?
"""

from formula import *
from semantics import *

trem_tarde = Atom('o trem chegou tarde')
onibus_estacao = Atom('tinha ônibus na estação')
atrasado_reuniao = Atom('josé chegou atrasado para a reunião')

# Se o trem chegou tarde e não tinha ônibus na estação, então João chegou atrasado para a reunião.
premissa1 = Implies(And(trem_tarde, Not(onibus_estacao)), atrasado_reuniao)

# João não chegou atrasado para a reunião.
premissa2 = Not(atrasado_reuniao)

# O trem chegou tarde na estação.
premissa3 = trem_tarde

# tinha ônibus na estação
conclusao = onibus_estacao

print(premissa1)
print(premissa2)
print(premissa3)
print(conclusao, '?')


print(is_logical_consequence([premissa1, premissa2, premissa3], conclusao))
