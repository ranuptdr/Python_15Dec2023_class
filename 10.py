# class Defination
class PythonProgrammingLanguage(): # ClassName always be in PascalCase Pattern
    #1. property  = Variable
    languagename = 'Python'
    devloper = 'Guido van Rossum'
    Year = '1991'

    #2. construsctor
    # constructor is a special method whose name is __init___ 
    
    #3. Method/Function (functionName always be in camelCase Pattern)
    def pyLanguage(self):  # always put first argument as self, self is internal object
        print(f' language name is {self.languagename}')
        print(f"Python devloper is {self.devloper}")
        print(f'The language was finally released in {self.Year}')
    pass
# Create instance of A class create class object 
# classobject = className()
co = PythonProgrammingLanguage() # co is a external clas object
# classobject.method
co.pyLanguage()

    