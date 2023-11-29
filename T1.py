class Circle: # Defined a class named  as Circle
    def __init__(self, radi_lt): # Constructor
        self.radi_lt = radi_lt # Created an instance variable to Circle class
        print("Assigned list: ",radi_lt) # displaying the argument
final_user_list = [10,501,22,37,100,999,87,351] # predefined list or We can also take the input from the users using input()
circle_value = Circle(final_user_list)# calling the Class and passing the list
