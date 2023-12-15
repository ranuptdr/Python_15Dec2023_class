# class Defination
class BankCustomer(): # ClassName always be in PascalCase Pattern
    #1. property  = Variable
    name = ''
    account_number = ''
    account_balance = ''
    
    #2. construsctor
    # constructor is a special method whose name is __init___ 
    def __init__(self,x,y,z): # always put first argument as self 
        # self is internal object
        self.name =x  # constructor initialize the property 
        self.account_number = y
        self.account_balance = z
    
    #3. Method/Function (functionName always be in camelCase Pattern)
    def customer(self):  # always put first argument as self, self is internal object
        print(f"customer name is {self.name}")
        print(f"customer account number is {self.account_number}")
        print(f'customer account balance is {self.account_balance}')
    pass
# Create instance of A class create class object 
# classobject = className()
co = BankCustomer("Ranu",123456789,110000) # co is a external clas object
# classobject.method()
co.customer()
