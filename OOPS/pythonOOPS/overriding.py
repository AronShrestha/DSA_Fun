class A:
    def show(self):
        print("I'm in A")

class B(A):
    def show(self):
        print("I'm in B")



b = B()
b.show()