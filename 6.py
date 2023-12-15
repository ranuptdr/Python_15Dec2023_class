# class Defination
class Student(): # PascalCase
    #1. property = variable
    name = ''
    surname = ''
    classs = ''
    Rollnumber = ''
    #2. constructor 
    # constructor is a special method whose name is __init___ 
    def __init__(self,fn,ln,clss,rno):  # always put first argument as self
        self.name = fn # constructor initialize the property 
        self.surname = ln # constructor initialize the property 
        self.classs = clss # constructor initialize the property 
        self.Rollnumber = rno # constructor initialize the property 
    #3. Method / function  (functionName always be in camelCase Pattern)
    def detail(self):  # always put first argument as self
        print(f"student name is {self.name}")
        print(f"student surname is {self.surname}")
        print(f'student class is {self.classs}')
        print(f'''student RollNumber is {self.Rollnumber}''')

# Creating instance "or" create class object
#classobject = className()
std = Student("Ranu","Patidar","12th",10)  
# classobject.method
std.detail()
    