# 1. In your own words, describe what a function is
"reusable code instructions" # answer

# re-usable code. Only runs when called. 
def starterFunction(): # our function definition/ instructions
    print("ian") # instruction 1
    print(2+2) # insturction 2
    print("all done the program") # instruction 3

#starterFunction() # our function call

# 2. What are function parameters and arguments and describe
# the difference between the 2. 
"function parameter is a placeholder- goes in function definition."
"function argument is the acutal data- goes in function call."

def addTwo(randomNumber):
    print(randomNumber + 2) # add 2 to the random number

def addtwo(randNumber): 
    print(randNumber +2) # rougihroihgowihn

#addtwo(2)

# 3. write a function that will print out a welcome message
# that includes a users name. You will need to use parameters and arguments

def welcome_msg(username):
    print('welcome '+ username + ' to coding class.')
    print('have a great day')

#welcome_msg('Wade Briscoe')
#welcome_msg('Tey')

# 4. Write a function that will do a calculation that takes 3 parameters.
# Your function can do any of the arithmatic operators (add, subtract, multiply, divide)

def calculate(randNumber, randomNumber2, randomNumber3): 
    print(randNumber +randomNumber2 + randomNumber3)

#calculate(7,12,12) # 7 100 700

# 5. Write a function that will output a message to a user, telling them
# what class they have next after this one. this code should use a 
# variable to pass a value into the parameter of a function. The variable should
# be real, user data- not hard coded data.

def userMsg():
    nextClass = input('what is your next class.')
    print("you have " + nextClass +" after this.")
   
    
userMsg()