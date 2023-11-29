class Squareproperties:
    def __init__(self, side_length):
        self.side_length = side_length # created an instance of the Square class
    def area(self): # medthod 1 was caluculating the area of square
        return self.side_length ** 2  # Area of a square = side length * side length
    def perimeter(self): # medthod 2 was caluculating the area of square
        return 4 * self.side_length  # Perimeter of a square = 4 * side length
side_length_users = int(input("Side length for square from user: ")) # Taking  length of sqaure value input from user
square = Squareproperties(side_length_users)  # Creating an instance for the Square class and passing the side length from user
# Calculate the area and perimeter using the methods
square_area = square.area() #from the class we are calling the area(methodD1)
square_perimeter = square.perimeter() #from the class we are calling the perimeter(methodD1)
print(f"area of the square was: {square_area} and ,perimeter of the square was: {square_perimeter}")

