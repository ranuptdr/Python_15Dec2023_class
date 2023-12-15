# class Defination
class Song(): # ClassName always be in PascalCase Pattern
    #1. property  = Variable
    title = ''
    artist = ''
    
    #2. construsctor
    # constructor is a special method whose name is __init___ 
    def __init__(self,x,y): # always put first argument as self 
        # self is internal object
        self.title =x  # constructor initialize the property 
        self.artist =y
    #3. Method/Function (functionName always be in camelCase Pattern)
    def s(self):  # always put first argument as self, self is internal object
        print(f"song name is {self.title}")
        print(f'song artist is {self.artist}')
    pass
# Create instance of A class create class object 
# classobject = className()
co = Song("Gaadi kaali","Neha Kakkar") # co is a external clas object
# classobject.method()
co.s()
