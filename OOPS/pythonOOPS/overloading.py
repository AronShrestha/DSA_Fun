class Area:
    def find_area(self, a=None, b=None):
        if a!=None and b!=None:
            print("Area of rectangle ", a*b)
        elif a!=None:
            print("Area square ", a*a)
        else:
            print("Sorry ")


# a = Area()
# a.find_area(5,9)
class A:
    def area(self,*arg):
        print(type(arg))
        print(arg)
        print(*arg)
        print(len(arg))
        if len(arg)>1:
            
            temp=1
            for i in range(len(arg)):
                temp*=arg[i]
            print(temp)
        elif len(arg)==1:
            print(arg[0]*arg[0])
  
        else:
            print("sorry")

# a =A()
# a.area(1,2)


# more on packing and unpacking

def A(*arg):
    print(arg)
    print(type(arg))
    B(*arg)

# A("abc",1,2,3,4)
# A(["abc",1,2,3,4])

def B(a,b,c):
    print(a,b,c)


# A(1,2,3)

# kwargs
def func(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

# func(a=2,b=4,c="a")
a={
    "A":1,
    1:"B",
    2:2
}
b={
    "A":"a",
    "B": "b",
    "C":"c"
}
def funwrong(a,b,c): #wrong
    print(a,b,c)
 
def funright(A,B,C):
    print(A,B,C)


# fun(**a)
funright(**b)