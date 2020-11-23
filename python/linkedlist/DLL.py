class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def setHead(self, node):
        # Write your code here.
        if self.head is None:
            self.head = node
			self.tail = node
			return
        self.insertBefore(self.head, node)
		
    def setTail(self, node):
        # Write your code here.
        if self.tail is None:
            self.setHead(node)
			return
        self.insertAfter(self.tail, node)
		
    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        
        
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert
		
		
    def insertAtPosition(self, position, nodeToInsert):
        
		if position == 1:
			self.setHead(nodeToInsert)
			return
		node = self.head
		currentPostition = 1
		while node is not None and currentPostition != position:
			node = node.next
			currentPostition += 1
		if node is not None:
			self.insertBefore(node, nodeToInsert)
		else:
			self.setTail(nodeToInsert)
		# Write your code here.
		# temp = self.head
		# for i in range(1,position-1):
		# temp = temp.next
		# if temp is not None:
		# self.insertAfter(temp, nodeToInsert)
		# else:
		# 	return None
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)



    def remove(self, node):
        if (node == self.head):
            self.head = self.head.next
        if (node == self.tail):
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def containsNodeWithValue(self, value):
        # Write your code here.
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None
    
    
    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None