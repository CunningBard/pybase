from option import Option

class LinkedList:
	def __init__(self, node = None, next = None):
		self._node = Option(node)
		self._next = Option(next)

	@property
	def node(self):
		return self._node

	@node.setter
	def node(self, val):
		self._node = Option(val)

	@property
	def next(self):
		return self._next

	@next.setter
	def next(self, val):
		self._next = Option(val)

	def contains(self, val) -> bool:
		if callable(val) and val(self.node):
			return True
		elif val == self.node:
			return True

		if self.next.is_some():
			return self.next.unwrap().contains(val)
		else:
			return False

	

	def get(self, fn) -> Option:
		if self.node.is_some() and fn(self.node.unwrap()):
				return self.node

		if self.next.is_some():
			return self.next.unwrap().get(fn)
		else:
			return Option()

	def filter(self, fn) -> list:
		if self.node.is_some():
			val = []
			if fn(self.node.unwrap()):
				val = [self.node.unwrap()]

			if self.next.is_some():
				val += self.next.unwrap().filter(fn)

			return val
		elif self.next.is_some():
			return self.next.unwrap().filter(fn)
		else:
			return []

	def add_to_last(self, val):
		if self.next.is_some():
			self.next.unwrap().add_to_last(val)
		else:
			self.next = LinkedList(val)

	def __repr__(self):
		return f"({self.node}) -> {self.next}"

	@staticmethod
	def from_list(ls: list):
		if len(ls) == 0:
			return LinkedList()

		first = LinkedList(ls.pop(0))
		for val in ls:
			first.add_to_last(val)

		return first

if __name__ == "__main__":
	ll = LinkedList.from_list(list(range(1, 101)))
	print(ll.filter(lambda x: x % 2 == 0))
