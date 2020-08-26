class Term:
    def __init__(self):
        pass


class Con(Term):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return isinstance(other, Con) and other.name == self.name

    def __hash__(self):
        return hash((self.name, 'con'))


class Var(Term):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return isinstance(other, Var) and other.name == self.name

    def __hash__(self):
        return hash((self.name, 'var'))


class Fun(Term):

    def __init__(self, name, args):
        super().__init__()
        self.name = name
        self.args = args

    def __str__(self):
        printable_function = str(self.name) + "("
        for i in range(len(self.args)):
            if i == len(self.args) - 1:
                printable_function = printable_function + str(self.args[i]) + ")"
            else:
                printable_function = printable_function + str(self.args[i]) + ', '
        return printable_function

    def __eq__(self, other):
        is_equal = isinstance(other, Fun) and len(other.args) == len(self.args)
        if not is_equal:
            return False
        for i in range(len(self.args)):
            if self.args[i] != other.args[i]:
                return False
        return True

    def __hash__(self):
        return hash(tuple(self.args) + (self.name, 'fun'))
