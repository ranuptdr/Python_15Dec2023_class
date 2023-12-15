# Class Definition
class Rectangle():  # PascalCase
    # 1. Property = variable
    length = ''
    width = ''
    
    # 2. Constructor
    def __init__(self, lth, wth):  # always put the first argument as self
        self.length = lth
        self.width = wth

    # 3. Method / function  (functionName always be in camelCase Pattern)
    def square(self):  # always put the first argument as self
        print(f'square length is {self.length}')
        print(f'square width is {self.width}')

# Creating instance "or" create class object
# classobject = className()
co = Rectangle(10, 20)
# classobject.method
co.square()