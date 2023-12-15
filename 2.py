# class Defination
class Dog:  # ClassName always be in PascalCase Pattern
    #1 Property
    name = ''
    age = ''
    color = ''

    #2 constructor
    # constructor is a special method whose name is __init___
    def __init__(self,Name,Age,Color):# Always put first argument as self & Name,age,color is formal argument
        self.name = Name #  constructor initilize the property
        self.age = Age #  constructor initilize the property
        self.color = Color #  constructor initilize the property
    #3 method/function (functionName always be in camelCase Pattern)
    def someInformation(self): # Always put first argument as self
        print(f"name is {self.name} and age is {self.age}  and color is {self.color}")

# Creating instance "or" create class object
#classobject = className()
petanimal = Dog("Jacky","1 year","Black")  # Jacky,1 year,black is actualargument
# classobject.method
petanimal.someInformation()