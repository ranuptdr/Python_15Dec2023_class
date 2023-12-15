# Class Definition
class Circle():
    # Property (variable)
    radius = 0.0

    # Constructor
    def __init__(self, x):
        # self is the internal object, and it initializes the property 'radius'
        self.radius = x

    # Method/Function
    def c(self):
        # Displays the radius of the circle
        print(f"The radius of the circle is {self.radius}")

# Create an instance of the Circle class (class object)
co = Circle("5cm.")

# Call the method to display the radius
co.c()
