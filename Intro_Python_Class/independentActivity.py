
# read and review the following pages on Python lists. Use these to help you solve
# the questions. 

linkOne= 'https://www.w3schools.com/python/python_lists.asp'
linkTwo= 'https://afternerd.com/blog/python-lists-for-absolute-beginners/'

# Answers must be submitted by the end of class to recieve a grade. 
# when you submit your work, make sure your submit message is relevant and MAKES SENSE!

# REMEMBER TO USE WRITE CLEAN AND READABLE CODE!

# When ready, answer the following prompts, Good luck!

# 1.Create a simple list variable that contains 5 list items. It is up to you what will be in your list and what 
# data type they will be. 
# Some examples: favorite_atheletes, favorite_games, favorite_books, etc.  

myFoodList=["pizza ","burger ","cake ", "pop tarts"]
#print(myFoodList)

# what is a list?
# a list is a way to store multiple values in a variable. 

# 2. Find and print the specific item in each list based on their index in the list
# HINT you will need to use a python built-in function that specifically lets you find items in a Python list. 

# find and print index 3
zoo_animals = ['wolf','giraffe','hippo','eagle','parrot']

za=zoo_animals.index('eagle')
#print(za)

#print(zoo_animals[3])

# find and print index 1
sports_on_tv =['hockey','football','baseball','soccer','racing']



# find and print index 0
random_numbers = [10,100,12123, 1394, 1]

# 3. Create a program that will only print out the odd numbers in this list. 
# HINT- part of solving this is that you will need to use the range() function. 

# we know we need to find and print the odd numbers.
# range() functions 
number_list= [1,2,3,4,5,6,7,8,9,10]
r= range(0,10)

odd= [x for x in range(10) if x%2==0]
#print(odd)


# 4. You have been hired by amazon to be an engineer. Your first assignment is to fix their
# shopping cart function. Your goal is to create a line of code that will
# allow users to enter the item they want as a string value, and add it to the items that
# are already exist in the shopping_cart list variable. 
# Once the new item is entered, a list of all items in the cart should print out. 

# HINT - for this function you will need to use the append() function. 

shopping_cart = ['notebook', 'pens','tape','mousepad']

def updatingShoppingCart():
    add_item=input('please add and item to your cart')
    shopping_cart.append(add_item)
    print(shopping_cart)

# updatingShoppingCart()


# Python List - a data type that allows for storing multiple values in a vairable. 
# a Python lists uses [] square brackets for the values. 
number_list= [101,10239, 10394, 10394]
string_list=['kevin']
var_list=[number_list, string_list]

#print(var_list)

apples=[2.00,'apple description']
tvDinner=[4.00,'sphagetti and meatballs']
water=[3.00,'20 onces']

self_checkout_scanner=[apples, tvDinner, water]
#print(len(self_checkout_scanner))

# type of container
# objects, strings, other data types inside of list

#_______________________________________________________________________________

# create a function that will add a new list item to a checkout cart
# the user should be able to enter the name of the item and the price.
# your function should add the name of the item to the list of items
# you will also need to write code that will add all the prices of the items
# including the price of the new item.

# keywords: 
# we know we need to use a function
# list

# clues: 
# there are differents item
# have a piece of code that will add up all the item prices including the price of a new item.
# we need to ask if they want to add item. We can use input() function.
# starter code
list__of_items=['apple', 'orange','book']

apple_price= 1.00
orange_price= 3.00
book_price= 10.00

def uber_Eat_checkout():
    new_item_name= input('what else would you like to add to the food cart? ')
    new_item_price= float(input('what is the price of the new item? '))
    list__of_items.append(new_item_name)
    print("your new shopping cart:")
    print(list__of_items)
    print("your final total")
    print(apple_price + orange_price + book_price + new_item_price)


#user_response = input('would you like to add another item? ')
#if user_response=='yes':
 #   uber_Eat_checkout()
#else:
#    print('proceed to checkout')




# Create a function that when it is called will delete the mail
message_from_mom='hey, hope your day is good.'
message_from_school='open this for your grade'
message_from_job='congrats youve got the role'

mail= [message_from_mom,message_from_job,message_from_school]

def deleteMail():
    subtraction_number= int(input('how many emails do you want to delete? '))
    if subtraction_number > mail:
        print('you asking to delete more emails than you actually have.')
    else:
        confirm_deletion=input('are you sure you want to delete these messages? ')
        if confirm_deletion =='yes':
            remaining_mail= mail-subtraction_number
            print('your remaing mail is listed below.')
            print(remaining_mail)
        else:
            print('we wont delete your emails')

deleteMail()



