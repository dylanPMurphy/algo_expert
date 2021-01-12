def minHeightBst(array):
    return constructMinHeightBST(array, 0, len(array-1))

constructMinHeightBST(array, startIndex, endIndex):
    if endIndex < startIndex:
        return None
    
    midIndex = (endIndex+ startIndex)//2
    bst = BST(array[midIndex])
    bst.left = constructMinHeightBST(array, startIndex, midIndex)
    bst.right = constructMinHeightBST(array, midIndex, endIndex)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
