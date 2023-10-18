
# 1. In your own words, describe what a function is

# 2. What are function parameters and arguments and describe
# the difference between the 2. 

# 3. write a function that will print out a welcome message
# that includes a users name. You will need to use parameters and arguments

# 4. Write a function that will do a calculation that takes 3 parameters.
# Your function can do any of the arithmatic operators (add, subtract, multiply, divide)

# 5. Write a function that will output a message to a user, telling them
# what class they have next after this one. this code should use a 
# variable to pass a value into the parameter of a function. The variable should
# be real, user data- not hard coded data.  

def isClassOver(timeParameter):
    if timeParameter>11.30:
        print('class is over. Time to go.')
    else:
        print('no, lets keep going')

isClassOver(11.31)

def writeName(nameParameter):
    user_name= input('what is your name?')
    if not isinstance(nameParameter, (int, float)): 
        print('cannot be a number')
    else:
        print('hello ' + user_name)

#writeName('Ian')

def petNoise(petParameter):
    if petParameter== 'dog':
        print('woof woof')
    elif petParameter =='cat':
        print('meow')

#petNoise('cat')

