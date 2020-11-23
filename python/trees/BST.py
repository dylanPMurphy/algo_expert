# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		runner = self
		while runner:
			if value < runner.value:
				if runner.left == None:
					runner.left = BST(value)
					return self
				else:
					runner = runner.left
			else:
				if runner.right == None:
					runner.right = BST(value)
					return self
				else:
					runner = runner.right
		return self

	def contains(self, value):
		# Write your code here.
		runner = self
		while runner:
			if runner.value == value:
				return True
			elif value < runner.value:
				runner = runner.left
			else:
				runner = runner.right
		return False

	def remove(self, value, parentNode = None):
		runner = self
		while runner:
			
			if value < runner.value:
				parentNode = runner
				runner = runner.left
			elif value > runner.value:
				parentNode = runner
				runner = runner.right
			else:
				if runner.left is not None and runner.right is not None:
					runner.value = runner.right.getMinValue()
					runner.right.remove(runner.value, runner)
				elif parentNode is None:
					if runner.left is not None:
						runner.value = runner.left.value
						runner.right = runner.left.right
						runner.left = runner.left.left
					elif runner.right is not None:
						runner.value  = runner.right.value
						runner.left = runner.right.left
						runner.right = runner.right.right
					else:
						pass
				elif parentNode.left == runner:
					parentNode.left = runner.left if runner.left is not None else runner.right
				elif parentNode.right == runner:
					parentNode.right = runner.left if runner.left is not None else runner.right
				break
		return self
				
	def getMinValue(self):
		runner = self
		while runner.left is not None:
			runner = runner.left
		return runner.value
	def findClosestValueInBst(tree, target):
		return findClosestValueInBstHelper(tree, target, float("inf"))


	def findClosestValueInBstHelper(tree, target, closest):
	
		if tree is None:
			return closest
		if abs(target - closest)> abs(target- tree.value):
			closest = tree.value
		if target < tree.value:
			return findClosestValueInBstHelper(tree.left, target, closest)
		elif target > tree.value:
			return findClosestValueInBstHelper(tree.right, target, closest)
		else:
			return closest
tree = BST(23)
tree.insert(234).insert(234235).insert(12).insert(12242).insert(14232).insert(122).insert(112).insert(12)
print(tree.contains(234))

print(tree.contains(23))
print(tree.contains(24))
tree.remove(23)
tree.remove(234)
print(tree.contains(23))
print(tree.contains(234))
