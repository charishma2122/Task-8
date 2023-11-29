# Calculating circle properties
circle_radius = int(input("Circle radius from user: ")) # Taking  circles radius input from user
class Circle:
    def __init__(self): # initializing constructor
        self.__pi = 3.141  # predefined pi value
    def circle_area(self, radius): # Method1 for calulating the circle area
        area = self.__pi * (radius ** 2) # Area = π×radius**2
        return area # output was area from this method , to use further
    def circle_circum(self, radius): # Method2 for calulating the circumference area
        circumference = 2 * self.__pi * radius # circum = 2*π×radius
        return circumference # output was area from this method , to use further this output
circle_prop = Circle() # calling the class
print("circle area:", circle_prop.circle_area(circle_radius)) # from the class we are calling area method to display the output
print("circle circumference:", circle_prop.circle_circum(circle_radius))  #from the class we are calling circum method to display the output

