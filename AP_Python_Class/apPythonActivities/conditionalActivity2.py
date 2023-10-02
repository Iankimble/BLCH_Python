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

# keywords: function, conditional statement, argument, float
# clues: we need to send a message; if its time to or stay.

def check_time(current_time):
    if current_time > 11.30:
        print('time to go. Have a good weekend.') 
    else:
        print('class is still in session.')

# check_time(12.10)

# 2. Write a function that uses a conditional statement. 
# your function should determine what type of pet a user has depending on the data provided by the user
# passed into the functions argument. 
# IF the user types in "woof", the function should return a message saying that it is a dog.
# IF the user types in "meow", the function should return a message saying that it is a cat.
# ELSE, if it is none of the animal sounds the function should return a message saying it doesn't 
# know what the animal is. 

# keywords = functions, conditional statement, argument, return,
# clues = we need to return a message depending on the condition.
# clues = the prompt tells us what to look for- animal sounds/ words.

def pet_noise():
    noise= input('type in animal noise.')
    if noise=="woof":
        print(' you have a dog.')     
    elif noise =="meow":
        print('you cat')
    elif noise =="quack quack":
        print("you have a duck")
    else:
        print('I dont know that animals')

#pet_noise()

def dominos_website_coupon():
    print('Do you have a coupon code for your order? please enter it.')
    coupon_code= input('enter your coupon.')
    if coupon_code=="LRGPZZA":
        print("congrats you get a free drink")     
    elif coupon_code=="BOGO":
        print("congrats, you can order another pizza for free")
    elif coupon_code =="WNGS":
        print("congrats, you will get a free brownie with you wings.")
    else:
        print('code is invalid or you did not put in coupon code.')

#dominos_website_coupon()

def local_places_by_direction():
    user_direction= input('which way are you going?')
    if user_direction=='right':
        print("your going into the direction of a pizza shop.")
    elif user_direction=='left':
        print('You are going into the direciton of a school.')
    elif user_direction=='straight':
        print("you are waling towards the church")
    elif user_direction=='backwards':
        print('you are going backwards')
    else:
        print("I dont know where that is. Please provide a direction.")

#local_places_by_direction()

# 3. Write a function that will take in a user name and height as parameters. 
# Your function should evaluate and determine if the user is tall in enough to get on a roller coster.
# IF the user is over 5.5, the function should return a custom message saying the user's name
# and a message "welcome please buckle up".
# ELSE if they they are not, return a message apologizing to the user saying they are not tall enough.

name = input('what is your name? ')
height= float(input('what is your height? '))

def rollercoaster_requiremets(name, height):
    if height > 5.5:
        print('welcome aboard. Buckle up,' + name)
    else:
        print('sorry but you are too small to get on this ride.')
        print('Please come back when your taller.')

# rollercoaster_requiremets(name, height)