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
        pass

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self
