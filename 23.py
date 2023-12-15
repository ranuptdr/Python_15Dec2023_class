# class Defination
class Bike(): # ClassName always be in PascalCase Pattern
    #1. property  = Variable
    company = 'Apache'
    Model = 'TVS Apache RTR 160 4V'
    Price = 125000
    #2. construsctor
    # constructor is a special method whose name is __init___ 
    # always put first argument as self 
    # self is internal object
    # constructor initialize the property 
    
    #3. Method/Function (functionName always be in camelCase Pattern)
    def b(self):  # always put first argument as self, self is internal object
        print(f" {self.company} {self.Model} {self.Price}")
    pass
# Create instance of A class create class object 
# classobject = className()
co = Bike() # co is a external clas object
# classobject.method()
co.b()