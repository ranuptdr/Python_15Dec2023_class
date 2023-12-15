# class Defination
class Laptop(): # ClassName always be in PascalCase Pattern
    #1. property  = Variable
    brand = ''
    model = ""
    price = ''
    
    #2. construsctor
    # constructor is a special method whose name is __init___ 
    def __init__(self,x,y,z): # always put first argument as self 
        # self is internal object
        # constructor initialize the property 
        self.brand = x
        self.model = y
        self.price = z
    
    #3. Method/Function (functionName always be in camelCase Pattern)
    def detail(self):  # always put first argument as self, self is internal object
        print(f"Laptop name is {self.brand} model is {self.model} price is {self.price}")
    pass
# Create instance of A class create class object 
# classobject = className()
co = Laptop("Dell",'XPS 13',50000) # co is a external clas object
# classobject.method()
co.detail()
