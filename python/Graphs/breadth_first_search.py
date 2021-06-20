
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        fifo = [self]
        while len(fifo) > 0:
            current = fifo.pop(0)
            array.append(current.name)
            for child in current.children:
                fifo.append(child)
        return array