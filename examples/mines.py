from semantics import *
from typing import List
from typing import Union

"""Campo Minado é um jogo em que o objetivo é limpar uma grade sem detonar nenhuma mina.
O jogador é apresentado inicialmente com uma grade de quadrados indiferenciados.
Alguns quadrados selecionados aleatoriamente, desconhecidos pelo jogador, são designados para conter minas.
Normalmente, o tamanho da grade e o número de minas são definidos previamente pelo usuário, digitando os números ou
selecionando os níveis de habilidade definidos, dependendo da implementação. O tamanho da grade geralmente é
selecionável pelo usuário como uma maneira de ajustar o nível de dificuldade.

O jogo é jogado revelando quadrados da grade através de cliques. Se um quadrado contendo uma mina for revelado,
o jogador perde o jogo. Se nenhuma mina for revelada, um dígito será exibido no quadrado, indicando quantos quadrados
adjacentes contêm minas; se não houver minas adjacentes, o quadrado ficará em branco.
O jogador usa essas informações para deduzir o conteúdo de outros quadrados e pode revelar com segurança cada quadrado
ou marcar o quadrado como contendo uma mina."""

"""O objetivo deste projeto é implementar programa para descobrir posições de minas. Dado um tabuleiro intermediário 
durante um jogo (ou seja, um tabuleiro com alguns quadrados revelados indicando o número de minas adjacentes), 
o programa deve dizer qual dos quadrados não revelados deve necessariamente conter uma mina e qual dos quadrados não
 revelados não pode ter mina. Para facilitar, você pode assumir que o campo tem no máximo 3 minas. """

"""
A entrada pode ser pode um arquivo ou direto no código.
A entrada a partir de um arquivo possui apenas valores inteiros separados por espaços em branco.
A primeira linha contém dois valores n, m representando o tamanho da grade (n linhas, m colunas).
Depois disso, n linhas com m inteiros cada seguem. 
Se o inteiro na posição (i, j) for -1, significa que é um quadrado não revelado. 
Se for um 0 <= k <= 3, significa que é um quadrado revelado e k de seus vizinhos são minas. 
Como exemplo, considere a seguinte entrada:
4 4
-1 -1 -1 -1
-1 -1 -1 -1
-1 1 1 1
-1 1 0 0

No código, a entrada pode ser representada da seguinte forma:
my_grid = [[-1, -1, -1, -1],
           [-1, -1, -1, -1],
           [-1, 1, 1, 1],
           [-1, 1, 0, 0]]
"""

my_grid = [[-1, -1, -1, -1],
           [-1, -1, -1, -1],
           [-1, 1, 1, 1],
           [-1, 1, 0, 0]]


# atom 0_0 denotes that there is a mine in square (0,0)
# atom 0_1 denotes that there is a mine in square (0,1)


# there is no mine in squares with number different from -1:

def no_mines(grid):
    premises = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != -1:
                premises = premises + [Not(Atom(str(i) + '_' + str(j)))]
    return premises


# if a square (i, j) has number k, there is exactly k mines adjacent to (i, j):

def mines_neighborhood(grid):
    premises = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                premises = premises + at_least_one(i, j)
                premises = premises + at_most_one(i, j)
            if grid[i][j] == 2:
                pass
                # ======== YOUR CODE HERE ========
            if grid[i][j] == 3:
                pass
                # ======== YOUR CODE HERE ========

    return premises


# at most one mine is adjacent to (i, j):

def at_most_one(i, j):
    neighbors = get_adjacent_cells(i, j)
    neighbors.remove((i, j))
    neighbors.sort()
    formulas = []
    for neighbor1 in neighbors:
        for neighbor2 in neighbors:
            if neighbor1 < neighbor2:
                formulas = formulas + [Not(And(Atom(str(neighbor1[0]) + '_' + str(neighbor1[1])),
                                               Atom(str(neighbor2[0]) + '_' + str(neighbor2[1]))))]
    return formulas


# at least one mine is adjacent to (i, j):

def at_least_one(i, j):  # -> List[Formula]
    neighbors = get_adjacent_cells(i, j)
    neighbors.remove((i, j))
    neighbors.sort()
    atoms = []
    for neighbor in neighbors:
        atoms.append(Atom(str(neighbor[0]) + '_' + str(neighbor[1])))
    final_formula = atoms[0]
    for atom in atoms:
        if atom != atoms[0]:
            final_formula = Or(atom, final_formula)
    return [final_formula]


def get_adjacent_cells(i, j):
    adjacent_cells = [(i + k, j + m) for k in [-1, 0, 1] for m in [-1, 0, 1] if 0 <= i + k <= 3 and 0 <= j + m <= 3]
    return adjacent_cells


# print(get_adjacent_cells(0, 0))
print('premises in no_mines(my_grid): ')
for premise in no_mines(my_grid):
    print(premise)

print('premises in mines_neighborhood(my_grid) ')
for premise in mines_neighborhood(my_grid):
    print(premise)


print(is_logical_consequence(no_mines(my_grid) + mines_neighborhood(my_grid), Atom('1_2')))
print(is_logical_consequence(no_mines(my_grid) + mines_neighborhood(my_grid), Not(Atom('1_2'))))
print(is_logical_consequence(no_mines(my_grid) + mines_neighborhood(my_grid), Atom('1_3')))
print(is_logical_consequence(no_mines(my_grid) + mines_neighborhood(my_grid), Not(Atom('1_3'))))
print(is_logical_consequence(no_mines(my_grid) + mines_neighborhood(my_grid), Atom('2_0')))
print(is_logical_consequence(no_mines(my_grid) + mines_neighborhood(my_grid), Not(Atom('2_0'))))
print(is_logical_consequence(no_mines(my_grid) + mines_neighborhood(my_grid), Atom('3_0')))
print(is_logical_consequence(no_mines(my_grid) + mines_neighborhood(my_grid), Not(Atom('3_0'))))
# ======== YOUR CODE HERE ========
