# class Defination
class Movie(): # ClassName always be in PascalCase Pattern
    #1. property  = Variable
    name = "Animal"
    
    #2. construsctor
    # constructor is a special method whose name is __init___ 
    
    #3. Method/Function (functionName always be in camelCase Pattern)
    def M(self):  # always put first argument as self, self is internal object
        print(f"movie name is {self.name}")
    pass
# Create instance of A class create class object 
# classobject = className()
co = Movie() # co is a external clas object
# classobject.method()
co.M()
