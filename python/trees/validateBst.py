def validateBst(tree):
    return bstHelper(tree, float('-inf'), float('inf'))

def bstHelper(tree, min, max):
	if tree is None: 
		return True
	if tree.value < min or tree.value >= max:
		return False
	
	leftIsValid = bstHelper(tree.left, min, tree.value)

	return leftIsValid and bstHelper(tree.right, tree.value, max)