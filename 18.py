# class Defination
class  MobilePhone(): # ClassName always be in PascalCase Pattern
    #1. property  = Variable
    brand = ''
    model = ''
    os = ''
    
    #2. construsctor
    # constructor is a special method whose name is __init___ 
    def __init__(self, x, y, z): # always put first argument as self 
        # self is internal object
        self.brand = x  # constructor initialize the property 
        self.model = y
        self.os = z
    
    #3. Method/Function (functionName always be in camelCase Pattern)
    def mo(self):  # always put first argument as self, self is internal object
        print(f"mobile brand is {self.brand}")
        print(f'mobile model is {self.model}')
        print(f'mobile os is {self.os}')
    pass
# Create instance of A class create class object 
# classobject = className()
co = MobilePhone("Samsung", "Galaxy S21", "Android") # co is a external clas object
# classobject.method()
co.mo()
