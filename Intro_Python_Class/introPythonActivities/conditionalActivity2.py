# 1. Write a function that uses a conditional statement. 
# Your function should return a message that will determine if
# class is over or not depending on the argument passed into your function.
# IF the time of class is greater than 11.30 (for AP section) or
# 1.00(for intro), your funcion should return a message saying 
# "class is over. Time to go". 
# ELSE if it is not, then your function should return a message saying
# "class is still in session."
# your function should also alow the user to put in the time. The time should be 
# formatted as a float. 

def check_class_status(class_time, section_type):
    if(section_type== 'AP' and class_time> 11.30) or (section_type=='Intro' and class_time > 1.00):
        return print('class is over. time to go')
    else:
        return print('class is in session')
    class_time= float(input('enter time'))
    section_type= input('enter class')

# check_class_status(2.00, 'Intro')

def class_Time_status():
    period_ends= 11.30
    time_of_class= float(input('what time is it?'))
    if time_of_class > period_ends:
        print('class is over time to go.')
    else:
        print('class is still in session.')

class_Time_status()

# keywords: float, function, argument,
# clues: we know we need to write a message about class times
# we know we need to write our times as floats 


 

# 2. Write a function that uses a conditional statement. 
# your function should determine what type a pet a user has depeding on the data provided by the user
# passed into the functions argument. 
# IF the user types in "woof", the function should return a message saying that it is a dog.
# IF the user types in "meow", the function should return a message saying that it is a cat.
# ELSE, if it is none of the animal sounds the function should return a message saying it doesn't 
# know what the animal is. 

# 3. Write a function that will take in a user name and height as parameters. 
# Your function should evaluate and determine if the user is tall in enough to get on a roller coster.
# IF the user is over 5.5, the function should return a custom message saying the user's name
# and a message "welcome please buckle up".
# ELSE if they they are not, return a message apologizing to the user saying they are not tall enough.