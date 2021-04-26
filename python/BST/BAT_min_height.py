def minHeightBst(array):
    return constructMinHeightBST(array, 0, len(array)-1)

def constructMinHeightBST(array, startIndex, endIndex):
    if endIndex < startIndex:
        return None
    
    midIndex = (endIndex + startIndex)//2
    bst = BST(array[midIndex])
    bst.left = constructMinHeightBST(array, startIndex, midIndex-1)
    bst.right = constructMinHeightBST(array, midIndex+1, endIndex)
    return bst
