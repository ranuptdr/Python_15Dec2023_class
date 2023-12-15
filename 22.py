# class Defination
class CoffeeMachine(): # ClassName always be in PascalCase Pattern
    #1. property  = Variable
    
    #2. construsctor
    # constructor is a special method whose name is __init___ 
    # always put first argument as self 
    def __init__(self, brand, model):  # self is internal object
        self.brand = brand
        self.model = model
    
    #3. Method/Function (functionName always be in camelCase Pattern)
    def c(self):  # always put first argument as self, self is internal object
        print(f"Making coffee with {self.brand} {self.model}")
    pass
# Create instance of A class create class object 
# classobject = className()
co = CoffeeMachine("Keurig", "K-Elite") # co is a external clas object
# classobject.method()
co.c()