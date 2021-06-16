def invertBinaryTree(tree):
    if tree is not None:
		invertBinaryTree(tree.left)
		invertBinaryTree(tree.right)
		temp= tree.right
		tree.right = tree.left
		tree.left = temp
		return tree
		

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

ss