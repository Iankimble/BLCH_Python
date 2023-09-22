# define the function. 
#You need to use the def keyword first
def welcome_msg():
    print('Welcome to the Python coding class.')

# call the function by writing it again. 
# This time around you dont need to write the instructions
#  or the def key word because it's already be written.

welcome_msg()


# Parameters are the placeholders for our data
# in functions.
def custom_welcome_msg(name):
    print("Good Morning " + name +". Welcome to Python class.")

# when we call, or execute our function we can pass an 
# argument into our function this is the actual data that
# our function will work on    
custom_welcome_msg('Ian')

# we can use all the data types as well as varialbes
# in functions

def calculator(numberA, numberB):
    print(numberA+numberB)

calculator(10,10)


# 1. In your own words, describe what a function is

# 2. What is are function parameters and arguments and describe
# the difference between the 2. 

# 3. write a function that will print out a welcome message
# that includes a users name. You will need to use parameters and arguments

# 4. Write a function that will do a calculation that takes 3 parameters.
# Your function can do any of the arithmatic operators (add, subtract, multiply, divide)

# 5. Write a function that will output a message to a user, telling them
# what class they have next after this one. this code should use a 
# variable to pass a value into the parameter of a function. The variable should
# be real, user data- not hard coded data.  



