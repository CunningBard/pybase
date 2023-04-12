

class Option:
	def __init__(self, val = None):
		self.val = val

	def unwrap(self):
		if self.val is not None:
			return self.val

		raise Exception("Unwrap on None")

	def is_some(self) -> bool:
		return self.val is not None

	def is_none(self) -> bool:
		return self.val is None

	def __repr__(self):
		return f"Some({self.val})" if self.val else "None"
