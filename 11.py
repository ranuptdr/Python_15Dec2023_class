# class Defination
class Employee(): # ClassName always be in PascalCase Pattern
    #1. property  = Variable
    name = ''
    salary = 0.0
    
    #2. construsctor
    # constructor is a special method whose name is __init___ 
    def __init__(self,x,y): # always put first argument as self 
        # self is internal object
        self.name = x  # constructor initialize the property 
        self.salary = y
    
    #3. Method/Function (functionName always be in camelCase Pattern)
    def person(self):  # always put first argument as self, self is internal object
        print(f'employe name is {self.name}')
        print(f'employe salary is {self.salary}')
    pass
# Create instance of A class create class object 
# classobject = className()
co = Employee("Ranu",50000) # co is a external clas object
# classobject.method()
co.person()
