# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    if tree.left:
		if tree.left.value >= tree.value:
			return False
		else:
			return validateBst(tree.left)
	elif tree.right:
		if tree.right.value < tree.value:
			return False
		else:
			return validateBst(tree.right)
	else:
		return True

