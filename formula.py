"""This module is designed to define formulas in propositional logic.
For example, the following piece of code creates an object representing (p v s):

formula1 = Or(Atom('p'), Atom('s'))

"""


class Atom:
    """
    This class represents propositional logic variables.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return isinstance(other, Atom) and other.name == self.name


class Implies:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + self.left.__str__() + " " + u"\u2192" + " " + self.right.__str__() + ")"

    def __eq__(self, other):
        return isinstance(other, Implies) and other.left == self.left and other.right == self.right


class Not:

    def __init__(self, inner):
        self.inner = inner

    def __str__(self):
        return "(" + u"\u00ac" + str(self.inner) + ")"

    def __eq__(self, other):
        return isinstance(other, Not) and other.inner == self.inner


class And:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + self.left.__str__() + " " + u"\u2227" + " " + self.right.__str__() + ")"

    def __eq__(self, other):
        return isinstance(other, And) and other.left == self.left and other.right == self.right


class Or:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + self.left.__str__() + " " + u"\u2228" + " " + self.right.__str__() + ")"

    def __eq__(self, other):
        return isinstance(other, Or) and other.left == self.left and other.right == self.right


class Iff:
    """
    Describes the 'if and only if' logical connective (<->) from propositional logic.
    A unicode value for <-> is 2194.
    """
    pass


class Xor:
    """
    Describes the xor (exclusive or) logical connective from propositional logic.
    A unicode value for xor is 2295.
    """
    pass
