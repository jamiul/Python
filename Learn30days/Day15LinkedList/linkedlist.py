# Create a Node
# Create Linked list
# Insert Node into Linked list
# print Linked list
class Node:
    def __init__(self,data=None): # Creation Node
        self.data = data
        self.next = None

class linkedList:
    """docstring for linkedList."""
    def __init__(self):
        self.head = None

    def insertNode(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printNode(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


node_1 = Node("Jamiul")
node_2 = Node("alam")
node_3 = Node("Rifat")
lin_1 = linkedList()
lin_1.insertNode(node_1)
lin_1.insertNode(node_2)
lin_1.insertNode(node_3)
lin_1.printNode()
