# class Defination
class StudentRecord(): # ClassName always be in PascalCase Pattern
    #1. property  = Variable
    name = ''
    age = ''
    grade = ''
    
    #2. construsctor
    # constructor is a special method whose name is __init___ 
    def __init__(self,x,y,z): # always put first argument as self 
        # self is internal object
        self.name =x  # constructor initialize the property 
        self.age = y
        self.grade = z
    #3. Method/Function (functionName always be in camelCase Pattern)
    def child(self):  # always put first argument as self, self is internal object
        print(f"name is {self.name}, age = {self.age}, grade = {self.grade}")
    pass
# Create instance of A class create class object 
# classobject = className()
co = StudentRecord("Tanisha", 14, "A+") # co is a external clas object
# classobject.method()
co.child()

    
