from semantics import *
import time

'''
No sudoku 4x4 é preciso preencher os quadrados de um grid de 4 linhas e 4 colunas com números de 1 a 4, 
e eles não podem se repetir na mesma linha, coluna ou subgrid.
'''

grid_test1 = [[0, 1, 4, 3],
              [4, 3, 2, 0],
              [1, 0, 3, 4],
              [3, 4, 1, 0]]

grid_test2 = [[0, 4, 3, 2],
              [0, 0, 1, 4],
              [2, 3, 0, 1],
              [4, 1, 2, 0]]

'''
grid_test1_ solution = [[2, 1, 4, 3],
                        [4, 3, 2, 1],
                        [1, 2, 3, 4],
                        [3, 4, 1, 2]]
'''


# atom 1_1_1 denotes that cell (1,1) is filled with 1
# atom 2_3_4 denotes that cell (2,3) is filled with 4


# auxiliary functions:

def and_all(list_formulas):
    """
    Returns a BIG AND formula from a list of formulas
    For example, if list_formulas is [Atom('1'), Atom('p'), Atom('r')], it returns
    And(And(Atom('1'), Atom('p')), Atom('r')).
    :param list_formulas: a list of formulas
    :return: And formula
    """
    first_formula = list_formulas[0]
    del list_formulas[0]
    for formula in list_formulas:
        first_formula = And(first_formula, formula)
    return first_formula


def or_all(list_formulas):
    """
    Returns a BIG OR of formulas from a list of formulas.
    For example, if list_formulas is [Atom('1'), Atom('p'), Atom('r')], it returns
    Or(Or(Atom('1'), Atom('p')), Atom('r')).
    :param list_formulas: a list of formulas
    :return: Or formula
    """
    first_formula = list_formulas[0]
    del list_formulas[0]
    for formula in list_formulas:
        first_formula = Or(first_formula, formula)
    return first_formula


# the solution must agree with the given digits:
def given_digits_constraints(grid):
    """
    Returns a formula that forces the truth values of atoms from given cells of the sudoku grid.
    For example, if cell 2,3 is filled with 1, then the final formula is of the form ... ∧ Atom('2_3_1') ∧ ...,
    which imposes that Atom('2_3_1') must be true.
    Besides, if cell 2,3 is filled with 1, then the final formula is of the form ... ∧ Not(Atom('2_3_2')) ∧ ...,
    which enforces that Atom('2_3_2') must be false.
    :param grid: sudoku grid
    :return: And formula
    """
    formulas_given = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != 0:
                formulas_given.append(Atom(str(i + 1) + '_' + str(j + 1) + '_' + str(grid[i][j])))
                for n in range(1, len(grid) + 1):
                    if n != grid[i][j]:
                        formulas_given.append(Not(Atom(str(i + 1) + '_' + str(j + 1) + '_' + str(n))))
    return and_all(formulas_given)


# each row must have all numbers:
def rows_constraints(grid):
    """
    Returns a formula imposing that each row must be filled with all numbers.
    For example, the final formula is of the form
    ... ∧ (Atom('2_1_4') v Atom('2_2_4') v Atom('2_3_4') v Atom('2_4_4')) ∧ ...,
    which forces that 4 is filled in some cell of row 2.
    :param grid: sudoku grid
    :return: And formula
    """
    formulas_rows = []
    for i in range(len(grid)):
        for n in range(len(grid)):
            or_list = []
            for j in range(len(grid)):
                or_list.append(Atom(str(i + 1) + '_' + str(j + 1) + '_' + str(n + 1)))
            formula_or = or_all(or_list)
            formulas_rows.append(formula_or)
    return and_all(formulas_rows)


# each cell cannot have two different numbers:
def cells_constraints(grid):
    """
    Returns a formula requiring that each cell cannot be filled with more than one number.
    For example, the final formula is of the form ... ∧ ¬(Atom('2_3_1') ∧ Atom('2_2_4')) ∧ ...,
    which represents that cell 2,3 cannot be filled with 1 and 4.
    :param grid: sudoku grid
    :return: And formula
    """
    formulas_cells = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            for n1 in range(len(grid) - 1):
                for n2 in range(n1 + 1, len(grid)):
                    formulas_cells.append(Not(And(Atom(str(i + 1) + '_' + str(j + 1) + '_' + str(n1 + 1)),
                                                  Atom(str(i + 1) + '_' + str(j + 1) + '_' + str(n2 + 1)))))
    return and_all(formulas_cells)


# each column has all digits:
def columns_constraints(grid):
    """
    Returns a formula imposing that each row must be filled with all numbers.
    For example, the final formula is of the form
    ... ∧ (Atom('2_1_4') v Atom('2_2_4') v Atom('2_3_4') v Atom('2_4_4')) ∧ ...,
    which forces that 4 is filled in some cell of row 2.
    :param grid: sudoku grid
    :return: And formula
    """
    columns_formulas = []
    for j in range(len(grid)):
        for n in range(len(grid)):
            or_list = []
            for i in range(len(grid)):
                or_list.append(Atom(str(i + 1) + '_' + str(j + 1) + '_' + str(n + 1)))
            or_formula = or_all(or_list)
            columns_formulas.append(or_formula)
    return and_all(columns_formulas)


def subgrids_constrains(grid):
    """
    Returns a formula imposing that each subgrid must be filled with all numbers.
    For example, the final formula is of the form
    ... ∧ (Atom('1_1_4') v Atom('1_2_4') v Atom('2_1_4') v Atom('2_2_4')) ∧ ...,
    which forces that 4 is filled in some cell of the first subgrid.
    :param grid: sudoku grid
    :return: And formula
    """
    subgrids_formulas = []
    for sl in range(2):
        for sc in range(2):
            for n in range(len(grid)):
                or_list = []
                for i in range(2):
                    for j in range(2):
                        or_list.append(Atom(str(sl * 2 + i + 1) + '_' + str(sc * 2 + j + 1) + '_' + str(n + 1)))
                or_formula = or_all(or_list)
                subgrids_formulas.append(or_formula)
    return and_all(subgrids_formulas)


def sudoku_solution(grid):
    """
    Prints the solution of a sudoku grid, if a solution exists. Otherwise, it prints that solution does not exist.
    It creates a formula imposing all constraints of the sudoku puzzle, and then uses a
    satisfiability checking procedure on this formula. The solution of the sudoku can be drawn from a interpretation
    that satisfies the formula.
    :param grid: sudoku grid
    """
    final_formula = And(
        And(
            And(
                given_digits_constraints(grid_test1),
                rows_constraints(grid_test1)
            ),
            And(
                cells_constraints(grid_test1),
                columns_constraints(grid_test1)
            ),
        ),
        subgrids_constrains(grid_test1)
    )
    solution = is_satisfiable(final_formula)
    if solution:
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    for n in range(len(grid)):
                        if solution[str(i + 1) + '_' + str(j + 1) + '_' + str(n + 1)]:
                            grid[i][j] = n + 1
                            break
        print(grid)
    else:
        print('Sudoku sem solução!')


start_time = time.time()
print('Solução do sudoku:')
sudoku_solution(grid_test1)
end_time = time.time()
print('Time:', end_time - start_time)
