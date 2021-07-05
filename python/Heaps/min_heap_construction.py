class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def parent(self, position):
        return position//2
    def leftChild(self, position):
        return (position *2)
    def rightChild(self, position):
        return (position *2) + 1


    def buildHeap(self, array):
        pass

    def siftDown(self, currentIdx, endIdx, heap):
        firstChildIdx = currentIdx * 2 + 1
        while firstChildIdx <= endIdx:
            secondChildIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1



    def siftUp(self):
        # Write your code here.
        pass

    def peek(self):
        # Write your code here.
        pass

    def remove(self):
        # Write your code here.
        pass

    def insert(self, value):
        # Write your code here.
        pass

    def swap( i , j ):
        pass
