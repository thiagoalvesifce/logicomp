"""A loja não estava aberta ou os funcionários não estavam atendendo ou,
a loja estava aberta e os funcionários estavam atendendo."""

from semantics import *

loja_aberta = Atom('a loja estava aberta')
funcionarios_atendendo = Atom('os funcionários estavam atendendo')


formula = Or(Or(Not(loja_aberta), Not(funcionarios_atendendo)), And(loja_aberta, funcionarios_atendendo))


print(is_valid(formula))
