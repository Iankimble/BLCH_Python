# What is a Computer Program?
# Insturctions that are read 
# by a computer to perform a specific task.
# What is Complexity and what is Abstraction?
# Complexity is the measure of resources used in processing.
# Abstraction is the process of simplifying complex processes.
# What is Syntax?
# Data Types
# Data Casting
# Built-in Functions
# User-Defined Functions
# Conditionals (if/ else)
# Loops (for/ while)

def info():
    name =input('what is you name? ')
    grade = int(input('what grade are you in? '))
    #if grade ==9:
    #    print('welcome '+ name + ' to intro python class.')
    #elif grade==10:
    #    print('welcome '+ name + ' to intro python class.')
    elif grade==11:
        print('welcome '+ name + ' to advance python class.')
    elif grade==12:
        print('welcome '+ name + ' to advance python class.')
    else:
        print('please retry and enter a grade.')

    if grade < 11:
        print('welcome '+ name + ' to intro python class.')
    elif grade > 10:
      print('welcome '+ name + ' to advance python class.')

info()