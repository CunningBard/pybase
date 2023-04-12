from linked_list import LinkedList
from option import Option

SPREAD_SIZE = 256

def true_hash(val):
	return hash(val) % SPREAD_SIZE

class HashNode:
	def __init__(self, key, val):
		self.key = key
		self.val = val


class HashMap:
	def __init__(self):
		self.values = [LinkedList()] * SPREAD_SIZE

	def get(self, key) -> Option:
		index = true_hash(key) 
		val = self.values[index]
		res = val.get(lambda x: x.key == key)

		if res.is_none():
			return Option()

		return Option(res.unwrap().val)

	def insert(self, key, value):
		index = true_hash(key)
		val = self.values[index]
		value = HashNode(key, value)
		if val.node.is_none():
			val.node = value
		else:
			val.add_to_last(value)

if __name__ == "__main__":
	hm = HashMap()
	hm.insert("sd", 1)
	hm.insert("wdf", 2)
	print(hm.get("wdf"))
