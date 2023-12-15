# class defination 
class Car: # PascleCase
    #1.1  Property = Variable
    brand = "" 
    model = '' 
    color = '' 
    
    #1.2  cunstructor
    #constructor is a especial method whose name is __init___ and used to initialize the property
    def __init__(self,brnd,mdl,clr): # Always put first argument as self 
        self.brand = brnd
        self.model = mdl
        self.color = clr

    #1.3  Method = Function (functionName always be in camelCase Pattern)
    def getMyBrand(self): # Always put first argument as self 
        print(f'brand is {self.brand}') #self is internal class object
        print(f"Model Year is {self.model}") #self is internal class object
        print(f'''color is {self.color}''') #self is internal class object
pass

#2. Create Class Object "or" create instance of class 
# classObject = className
co = Car("Audi",2023,"White") # co is a external clas object

# Call the method with classObject
# classObject.method(actualargument1,actualArgument2)
co.getMyBrand() 