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
