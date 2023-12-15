# class Defination
class Person(): # ClassName always be in PascalCase Pattern
    #1. property  = Variable
    name = ''
    age = ''
    
    #2. construsctor
    # constructor is a special method whose name is __init___ 
    def __init__(self,fname,Age): # always put first argument as self 
        # self is internal object
        self.name = fname  # constructor initialize the property 
        self.age = Age
    #3. Method/Function (functionName always be in camelCase Pattern)
    def prsn(self):  # always put first argument as self, self is internal object
        print(f'persion name is {self.name} and Age is {self.age}')
    pass
# Create instance of A class create class object 
# classobject = className()
pco = Person("jiyansh",5) # co is a external clas object
# classobject.method
pco.prsn()
