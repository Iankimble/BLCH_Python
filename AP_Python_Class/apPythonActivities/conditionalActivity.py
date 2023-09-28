# 1. What is the difference between 
# a parameter and an argument in a python function?

"parameter are placeholders in our function definition."
"We are expecting some data."
"An agrument is value or data that is sent to the function it's called."

# 2. In your own words, describe what 
# a conditional statement (if/else) is 

" a tool that allows you make"
"decesions depending on if a certain condition is met."

# 3. write a simple conditional state using a comparision operator(greater than, less than, etc. )

a= 200
b= 2

if b > a:
    print('B is greater than A')
else:
    print('B is not greater than A')

#name = input('Enter your name')

# if name =='Ian': # not the same ian- case sensative 
#   print('this is the correct name')
# else:
#   print("not my name")


# 4. Write a conditional statement for food in the refridgerator.
# your conditional statement should be wrapped in a function that takes one (1)
# parameter. The data type for this parameter should be true or false. 
# If there is food in the refridgerator, print time to cook. If there is 
# NOT food in the fridge, print time to shop. 
# When you call your function there should be an argument that accepts 
# a boolean. 

# boolean as an argument in our function (value will either true or false)

def foodInFridge(food):
    if food == True:
        print('Time to cook.')
    else:
        print('Time to shop.')

#foodInFridge(True)

# 5. Create a function that checks the inventory of cereal for a store. 
# your function should have a parameter that accepts an integer. In your function
# use a conditional statement to determine if you need to order more cereal.
# If there is more than 10 boxes, print "inventory full", else if there are less than 
# 10 boxes print "we need to order more cereal".

# keywords = parameter, integer, conditional statement(if/else) function, 10 cereal boxes

def check_cereal_inventory(quantity):
    if quantity > 10:
        print('inventory is full.')
    else:
        print('order more cereal.')

print('___________________________')
check_cereal_inventory(8)