class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
    
    def setNext(self, node):
        self.next = node
    
    def getNext(self):
        return self.next


    def reverse(self,head):
        """
        Reversing a linkedlist
        """
        prev = Node(head.value)
        next = Node(head.value)
        curr = head.getNext()
        while curr != None:
            next = curr.getNext()
            curr.next = prev 
            prev = curr
            curr = next 
        return curr 
    def merge(self,A,B):
        if A == None :
            print(f"returning B{B.value}")
            return B
        if B == None :
            print(f"returning A {A.value}")
            return A
        if A.value <= B.value:
            print(f"calling A {A.value} next ")
            A.next = self.merge(A.next, B)
            print(f"returning A {A.value}")
            
            return A 
        if B.value < A.value:
            print(f"calling B {B.value} next ")
            B.next = self.merge(A,B.next)
            print(f"returning A {B.value}")
            return B
        
    @staticmethod
    def display(temp):
        print("We are on displaying function")
        
        while temp != None:
            print(temp.value)
            temp = temp.getNext()


def IterativeMerge(A,B):
    node = Node()
    tempNode = node
    if A.value == None:
        tempNode.value = B.value
        B = B.next
    if B.value == None :
        tempNode.value = A.value 
        A = A.next
    if A.value < B.value:
        tempNode.value = A.value 
        A = A.next   
    else:
        tempNode.value = B.value
        B = B.next
    while A!= None and B!= None:
        if A.value < B.value:
            tempNode.next = A
            tempNode= tempNode.next

            A = A.next
        else:
            tempNode.next = B   
            tempNode= tempNode.next 
            B = B.next
    while A != None:
        tempNode.next = A
        tempNode= tempNode.next
        A = A.next
    while B != None:
        tempNode.next = B  
        tempNode = tempNode.next  
        B = B.next        
    
    return node





n1 = Node(1)
n2 = Node(8)
n3 = Node(22)
n4 = Node(40)
n1.setNext(n2)
n2.setNext(n3)
n3.setNext(n4)


n1_1 = Node(4)
n2_2 = Node(11)
n3_3 = Node(16)
n4_4 = Node(20)
n1_1.setNext(n2_2)
n2_2.setNext(n3_3)
n3_3.setNext(n4_4)
# n1.merge(n1, n1_1)

# sorted_node = IterativeMerge(n1,n1_1)
Node.display(n1)

n1.reverse(n1)
Node.display(n4)
# # n1.reverseLinkedlist(n1)
# n1.display(n1)
