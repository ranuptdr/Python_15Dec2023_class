# class Defination
class FamilyMember(): # ClassName always be in PascalCase Pattern
    #1. property  = Variable
    totalmember = ''

    #2. construsctor
    # constructor is a special method whose name is __init___ 
    def __init__(self,x): # always put first argument as self 
        # self is internal object
        self.totalmember = x  # constructor initialize the property 
    
    #3. Method/Function (functionName always be in camelCase Pattern)
    def fM(self):  # always put first argument as self, self is internal object
        print(f"MyFamily Totel Member is {self.totalmember}")
    pass
# Create instance of A class create class object 
# classobject = className()
co = FamilyMember(5) # co is a external clas object
# classobject.method()
co.fM()