# class Defination
class A(): # ClassName always be in PascalCase Pattern
    #1. property
    a = ''
    b = ''
    #2. construsctor
    # constructor is a special method whose name is __init___ 
    def __init__(self,x,y): # always put first argument as self & x,y is formal argument
        # self is internal object
        self.a =x  # constructor initialize the property 
        self.b =y  # constructor initialize the property 
        print('Hello')

    #3. Method/Function (functionName always be in camelCase Pattern)
    def addTwoNumber(self):  # always put first argument as self
        print(f"the sum of {self.a} and {self.b} is {self.a + self.b}")
    pass
''' Create instance of A class "or"
    create class object
''' 
# tripal string is a multiline comment
# classobject = className()
co = A(10,40) # actualargument1 = 10, actualargument2 = 40
# classobject.method
co.addTwoNumber()
# note :- The Parameters Passed while creating the object of a class will be received in the constructor of the class
    
