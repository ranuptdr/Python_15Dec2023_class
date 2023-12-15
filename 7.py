# Class Definition
class MathOperations():  # PascalCase
    # 1. Property = variable
    a = ''
    b = ""

    # 2. Constructor
    # Constructor is a special method whose name is __init___
    def __init__(self, x, y):  # always put the first argument as self
        self.a = x  # constructor initializes the property
        self.b = y  # constructor initializes the property

    # 3. Method / function  (functionName always be in camelCase Pattern)
    def sub(self):  # always put the first argument as self
        print(f'The difference of {self.a} and {self.b} is {self.a - self.b}')

# Creating instance "or" create class object
# classobject = className()
co = MathOperations(60,20)
# classobject.method
co.sub()