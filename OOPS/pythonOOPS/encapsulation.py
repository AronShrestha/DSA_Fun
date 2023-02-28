class Base:
    def __init__(self):
        self.a = "I am public variable"
        self._b = "I am protected variable"
        self.__c = " I am  private varaible"
    


# o = Base()
# print(o.a)
# print(o._b)
# print(o.__c)

class Student:

    #protected data members
    _name = None
    _rolll = None 
    _branch = None

    def __init__(self, name, roll, branch) -> None:
        self._name = name 
        self._roll = roll
        self._branch = branch
    
     # protected member function  
    
    def _displayRollAndBranch(self):
          # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)        

 
# derived class
class Geek(Student):
 
       # constructor
       def __init__(self, name, roll, branch):
            Student.__init__(self, name, roll, branch)
            # super().__init__(name, roll, branch)
         
       # public member function
       def displayDetails(self):
                   
                 # accessing protected data members of super class
                print("Name: ", self._name)
                   
                 # accessing protected member functions of super class
                self._displayRollAndBranch()  


obj = Geek("R2J", 1706256, "Information Technology")
 
# calling public member functions of the class
obj.displayDetails()
# obj._displayRollAndBranch()

# program to illustrate access modifiers of a class

# super class
class Super:
	
	# public data member
	var1 = None

	# protected data member
	_var2 = None
	
	# private data member
	__var3 = None
	
	# constructor
	def __init__(self, var1, var2, var3):
		self.var1 = var1
		self._var2 = var2
		self.__var3 = var3
	
	# public member function
	def displayPublicMembers(self):

		# accessing public data members
		print("Public Data Member: ", self.var1)
		
	# protected member function
	def _displayProtectedMembers(self):

		# accessing protected data members
		print("Protected Data Member: ", self._var2)
	
	# private member function
	def __displayPrivateMembers(self):

		# accessing private data members
		print("Private Data Member: ", self.__var3)

	# public member function
	def accessPrivateMembers(self):	
		
		# accessing private member function
		self.__displayPrivateMembers()

# derived class
class Sub(Super):

	# constructor
	def __init__(self, var1, var2, var3):
                super().__init__(var1,var2,var3)
				# Super.__init__(self, var1, var2, var3)
		
	# public member function
	def accessProtectedMembers(self):
				
				# accessing protected member functions of super class
				self._displayProtectedMembers()

# creating objects of the derived class	
obj = Sub("Geeks", 4, "Geeks !")

# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

# Object can access protected member
print("Object is accessing protected member:", obj._var2)

# object can not access private member, so it will generate Attribute error
#print(obj.__var3)
 