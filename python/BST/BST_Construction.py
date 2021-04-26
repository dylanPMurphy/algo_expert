class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		runner = self
		while runner is not None:
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
		while runner is not None:
			if runner.value == value:
				return True
			elif value < runner.value:
				runner = runner.left
			else:
				runner = runner.right
		return False

	def remove(self, value, parentNode = None):
		runner = self
		while runner is not None:
			
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

