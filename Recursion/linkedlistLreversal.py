class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def setNext(self, node):
        self.next = node
    
    def getNext(self):
        return self.next

    def reverseLinkedlist(self,node):
        if node == None or node.next == None:
            return node
        else:
            prev_node = self.reverseLinkedlist(node.next)
            print(f"node number return {prev_node.value}")
            node.next.next = node 
            node.next = None
            # return "1"
            return prev_node
        
    def display(self,node):
        print("We are on displaying function")
        temp = node
        while temp != None: 
            print(temp.value)
            temp = temp.getNext()



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.setNext(n2)
n2.setNext(n3)
n3.setNext(n4)
n4.setNext(n5)
n5.setNext(n6)
n1.display(n1)

print("*****************************************************")

n1.reverseLinkedlist(n1)
n6.display(n6)