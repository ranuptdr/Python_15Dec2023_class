# Class Definition
class EmailClient():  # ClassName always be in PascalCase Pattern
    # 1. Property = Variable
    username = ''
    Emailid = ''
    Password = ""
    
    # 2. Constructor
    # Constructor is a special method whose name is __init___ 
    def __init__(self, x, y, z):  # always put the first argument as self 
        # self is internal object
        self.username = x  # constructor initializes the property 
        self.Emailid = y
        self.Password = z
    
    # 3. Method/Function (functionName always be in camelCase Pattern)
    def display_info(self):  # always put the first argument as self, self is internal object
        print(f"Client username {self.username}, Email ID {self.Emailid}, Password {self.Password}")

# Create instance of EmailClient class, create class object 
# classobject = className()
co = EmailClient("Ranu", "ranu@gmail.com", "123")  # co is an external class object
# classobject.method()
co.display_info()
