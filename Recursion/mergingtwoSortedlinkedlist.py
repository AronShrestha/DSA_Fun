class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def setNext(self, node):
        self.next = node
    
    def getNext(self):
        return self.next

    def merge(self,A,B):
        if A == None :
            print(f"returning B{B.value}")
            return B
        if B == None :
            print(f"returning A {A.value}")
            return A
        if A.value < B.value:
            print(f"calling A {A.value} next ")
            A.next = self.merge(A.next, B)
            print(f"returning A {A.value}")
            
            return A 
        if B.value < A.value:
            print(f"calling B {B.value} next ")
            B.next = self.merge(A,B.next)
            print(f"returning A {B.value}")
            return B
        
    def display(self, node):
        print("We are on displaying function")
        temp = node
        while temp != None:
            print(temp.value)
            temp = temp.getNext()


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
n1.merge(n1, n1_1)


print("*****************************************************")

# n1.reverseLinkedlist(n1)
n1.display(n1)
