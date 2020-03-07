"""Quatro colegas precisam se reunir em algum dia útil da semana.
João pode na Segunda, Quarta ou Quinta.
Carol não pode na Quarta.
Ana não pode na Sexta.
Pedro não pode Terça nem Quinta.
Existe um dia que eles possam se reunir satisfazendo todas as demandas?"""


from semantics import *


meeting_monday = Atom('reuniao na segunda')
meeting_tuesday = Atom('reuniao na terça')
meeting_wednesday = Atom('reuniao na quarta')
meeting_thursday = Atom('reuniao na quinta')
meeting_friday = Atom('reuniao na sexta')

joao = Or(Or(meeting_monday, meeting_wednesday), meeting_thursday)
carol = Not(meeting_wednesday)
ana = Not(meeting_friday)
pedro = And(Not(meeting_tuesday), Not(meeting_thursday))

all_requirements = And(And(And(joao, carol), ana), pedro)

print(is_satisfiable(all_requirements))


