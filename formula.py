class Atom:

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return str(self.name)


class Implies:

	def __init__(self, left, right):
		self.left = left
		self.right = right

	def __str__(self):
		return "(" + self.left.__str__() + " " + u"\u2192" + " " + self.right.__str__() + ")"


class Not:

	def __init__(self, inner):
		self.inner = inner

	def __str__(self):
		return "(" + u"\u00ac" + str(self.inner) + ")"


class And:

	def __init__(self, left, right):
		self.left = left
		self.right = right

	def __str__(self):
		return "(" + self.left.__str__() + " " + u"\u2227" + " " + self.right.__str__() + ")"


class Or:

	def __init__(self, left, right):
		self.left = left
		self.right = right

	def __str__(self):
		return "(" + self.left.__str__() + " " + u"\u2228" + " " + self.right.__str__() + ")"
