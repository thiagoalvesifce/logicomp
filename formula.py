"""This module is designed to define formulas in propositional logic.
For example, the following piece of code creates an object representing (p v s).

formula1 = Or(Atom('p'), Atom('s'))


As another example, the piece of code below creates an object that represents (p → (p v s)).

formula2 = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
"""
# from typeguard import typechecked

class Formula:
    def __init__(self):
        pass
    # end def
# end class Formula


class Atom(Formula):
    """
    This class represents propositional logic variables.
    """

    def __init__(self, name: str):
        super().__init__()
        self.name = name
    # end def

    def __str__(self):
        return str(self.name)
    # end def

    def __eq__(self, other: Formula):
        return isinstance(other, Atom) and other.name == self.name
    # end def

    def __hash__(self):
        return hash((self.name, 'atom'))
    # end def
# end class Atom


class Implies(Formula):
    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right
    # end def

    def __str__(self):
        return "(" + self.left.__str__() + " " + u"\u2192" + " " + self.right.__str__() + ")"
    # end def

    def __eq__(self, other: Formula):
        return isinstance(other, Implies) and other.left == self.left and other.right == self.right
    # end def

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'implies'))
    # end def
# end class Implies


class Not(Formula):

    def __init__(self, inner: Formula):
        super().__init__()
        self.inner = inner
    # end def

    def __str__(self):
        return "(" + u"\u00ac" + str(self.inner) + ")"
    # end def

    def __eq__(self, other: Formula):
        return isinstance(other, Not) and other.inner == self.inner
    # end def

    def __hash__(self):
        return hash((hash(self.inner), 'not'))
    # end def
# end class Not


class And(Formula):
    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right
    # end def

    def __str__(self):
        return "(" + self.left.__str__() + " " + u"\u2227" + " " + self.right.__str__() + ")"
    # end def

    def __eq__(self, other: Formula):
        return isinstance(other, And) and other.left == self.left and other.right == self.right
    # end def

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'and'))
    # end def
# end class And


class Or(Formula):

    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right
    # end def

    def __str__(self):
        return "(" + self.left.__str__() + " " + u"\u2228" + " " + self.right.__str__() + ")"
    # end def

    def __eq__(self, other: Formula):
        return isinstance(other, Or) and other.left == self.left and other.right == self.right
    # end def

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'or'))
    # end def
# end class Or


class Iff:
    """
    Describes the 'if and only if' logical connective (<->) from propositional logic.
    Unicode value for <-> is 2194.
    """
    pass
# end class Iff


class Xor:
    """
    Describes the xor (exclusive or) logical connective from propositional logic.
    Unicode value for xor is 2295.
    """
    pass
# end class Xor
