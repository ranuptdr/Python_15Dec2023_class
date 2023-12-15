# Class Definition
class MovieTicket():  # ClassName always be in PascalCase Pattern
    # 1. Property = Variable
    movie = 'Animal'
    showtime = '12:10 PM '
    price = '500 rs'
    
    # 2. Constructor
    # Constructor is a special method whose name is __init__
    
    # 3. Method/Function (functionName always be in camelCase Pattern)
    def m(self):  # always put the first argument as self, self is an internal object
        print(f"Movie {self.movie}")
        print(f"Showtime {self.showtime}")
        print(f"Price {self.price}")

# Create instance of MovieTicket class, create class object 
# classobject = className()
co = MovieTicket()  # co is an external class object
# classobject.method()
co.m()


    
