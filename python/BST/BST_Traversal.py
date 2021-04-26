def inOrderTraverse(tree, array):
    # Write your code here.
    # (a) Inorder (Left, Root, Right) : 4 2 5 1 3
	if tree is not None:
		
		inOrderTraverse(tree.left, array)
		array.append(tree.value)
		inOrderTraverse(tree.right, array)
		
	return array
def preOrderTraverse(tree, array):
    # Write your code here.
    # (b) Preorder (Root, Left, Right) : 1 2 4 5 3
	if tree is not None:
		array.append(tree.value)
		preOrderTraverse(tree.left, array)
		preOrderTraverse(tree.right, array)
	return array
def postOrderTraverse(tree, array):
    # Write your code here.
	# (c) Postorder (Left, Right, Root) : 4 5 2 3 1
	if tree is not None:
		postOrderTraverse(tree.left, array)
		postOrderTraverse(tree.right, array)
		array.append(tree.value)
	return array