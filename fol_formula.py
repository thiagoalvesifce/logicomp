class FormulaFOL:
    def __init__(self):
        pass


class Atom(FormulaFOL):

    def __init__(self, name, args):
        super().__init__()
        self.name = name
        self.args = args

    def __str__(self):
        printable_predicate = str(self.name) + "("
        for i in range(len(self.args)):
            if i == len(self.args) - 1:
                printable_predicate = printable_predicate + str(self.args[i]) + ")"
            else:
                printable_predicate = printable_predicate + str(self.args[i]) + ', '
        return printable_predicate

    def __eq__(self, other):
        is_equal = isinstance(other, Atom) and len(other.args) == len(self.args)
        if not is_equal:
            return False
        for i in range(len(self.args)):
            if self.args[i] != other.args[i]:
                return False
        return True

    def __hash__(self):
        return hash(tuple(self.args) + (self.name, 'atom'))


class Implies(FormulaFOL):

    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + self.left.__str__() + " " + u"\u27F6" + " " + self.right.__str__() + ")"

    def __eq__(self, other):
        return isinstance(other, Implies) and other.left == self.left and other.right == self.right

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'implies'))


class Not(FormulaFOL):

    def __init__(self, inner):
        super().__init__()
        self.inner = inner

    def __str__(self):
        return "(" + u"\u00ac" + str(self.inner) + ")"

    def __eq__(self, other):
        return isinstance(other, Not) and other.inner == self.inner

    def __hash__(self):
        return hash((hash(self.inner), 'not'))


class And(FormulaFOL):

    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + self.left.__str__() + " " + u"\u2227" + " " + self.right.__str__() + ")"

    def __eq__(self, other):
        return isinstance(other, And) and other.left == self.left and other.right == self.right

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'and'))


class Or(FormulaFOL):

    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + self.left.__str__() + " " + u"\u2228" + " " + self.right.__str__() + ")"

    def __eq__(self, other):
        return isinstance(other, Or) and other.left == self.left and other.right == self.right

    def __hash__(self):
        return hash((hash(self.left), hash(self.right), 'or'))


class ForAll(FormulaFOL):

    def __init__(self, var, inner):
        super().__init__()
        self.inner = inner
        self.var = var

    def __str__(self):
        return "(" + u"\u2200" + str(self.var) + str(self.inner) + ")"

    def __eq__(self, other):
        return isinstance(other, ForAll) and other.inner == self.inner and other.var == self.var

    def __hash__(self):
        return hash((hash(self.inner), 'all', hash(self.var)))


class Exists(FormulaFOL):

    def __init__(self, var, inner):
        super().__init__()
        self.inner = inner
        self.var = var

    def __str__(self):
        return "(" + u"\u2203" + str(self.var) + str(self.inner) + ")"

    def __eq__(self, other):
        return isinstance(other, Exists) and other.var == self.var and other.inner == self.inner

    def __hash__(self):
        return hash((hash(self.inner), 'exists', hash(self.var)))
