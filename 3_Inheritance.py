# class defination 
class Parent(): # class name always be in PascalCase Pattern
    #1. Property
    surname = ''
    bloodGroup = ''

    #2. constructor
    # constructor is a special method whose name is __init___
    def __init__(self,sn,bg):
        self.surname = sn
        self.bloodGroup = bg

    #3. Method / Function (functionName always be in camelCase Pattern)


class Child(Parent): # class name always be in PascalCase Pattern
    #1. Property
    #2. constructor
    # constructor is a special method whose name is __init___

    #3. Method / Function (functionName always be in camelCase Pattern)
    def inharit(self):
        print(f" My surname is {self.surname} ")
        print(f" My bloodgroup is {self.bloodGroup} ")


# create class object or  Creating instances
#classobject = className()
childco = Child("patidar", 'o+ve')

# classobject.method()
childco.inharit()

