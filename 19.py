# class Defination
class Country(): # ClassName always be in PascalCase Pattern
    #1. property  = Variable
    name = ''
    population = ''
    capital = ''
    
    #2. construsctor
    # constructor is a special method whose name is __init___ 
    def __init__(self,x,y,z): # always put first argument as self 
        # self is internal object
        self.name = x  # constructor initialize the property 
        self.population = y
        self.capital = z 

    
    #3. Method/Function (functionName always be in camelCase Pattern)
    def c(self):  # always put first argument as self, self is internal object
        print(f"country name is {self.name}")
        print(f'country population is {self.population}')
        print(f"country capital is {self.capital}")
    pass
# Create instance of A class create class object 
# classobject = className()
co = Country("India", 1425775850, "New Delhi") # co is a external clas object
# classobject.method()
co.c()

    

