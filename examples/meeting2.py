"""Quatro colegas precisam se reunir em algum dia útil da semana.
Adam só pode Segunda ou Quarta.
Bridget não pode na Quarta.
Charles não pode na Sexta.
David só pode na Quinta ou na Sexta.
Existe um dia que eles possam se reunir satisfazendo todas as demandas?"""

from semantics import *

meeting_monday = Atom('reuniao na segunda')
meeting_tuesday = Atom('reuniao na terca')
meeting_wednesday = Atom('reuniao na quarta')
meeting_thursday = Atom('reuniao na quinta')
meeting_friday = Atom('reuniao na sexta')

# Adam can ONLY meet on Monday or Wednesday. So, he cannot meet on the other days.
adam = And(And(And(Or(meeting_monday, meeting_wednesday), Not(meeting_tuesday)), Not(meeting_thursday)),
           Not(meeting_friday))
bridget = Not(meeting_wednesday)
charles = Not(meeting_friday)

# David's constraints are similar to Adam's ones.
david = And(
            And(
                And(
                    Or(
                        meeting_thursday,
                        meeting_friday
                    ),
                    Not(meeting_wednesday)
                ),
                Not(meeting_tuesday)
            ),
            Not(meeting_monday)
        )

all_requirements = And(And(And(adam, bridget), charles), david)

print(satisfiability_brute_force(all_requirements))
