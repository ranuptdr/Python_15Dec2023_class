# Class Definition
class Restaurant():  # ClassName always be in PascalCase Pattern
    # 1. Property = Variable
    name = ''
    contact_number = ''  # Corrected the variable name
    address = ''         # Corrected the variable name
    
    # 2. Constructor
    # Constructor is a special method whose name is __init__
    def __init__(self, a, b, c):  # always put the first argument as self
        # self is an internal object
        self.name = a  # constructor initializes the property
        self.contact_number = b  # Corrected the variable name
        self.address = c          # Corrected the variable name
    
    # 3. Method/Function (functionName always be in camelCase Pattern)
    def display_info(self):  # always put the first argument as self, self is an internal object
        print(f"Restaurant name is {self.name}")
        print(f"Contact number is {self.contact_number}")
        print(f"Address is {self.address}")

# Create instance of Restaurant class, create class object
# classobject = className()
co = Restaurant("Sky Heaven", 9876543210, "Mandsaur")  # co is an external class object
# classobject.method()
co.display_info()
