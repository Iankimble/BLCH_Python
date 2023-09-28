# 1. What is the difference between 
# a parameter and an argument in a python function

"parameter is a place holder."
"argument is the actual data."

"parameter is variable listed inside of function definition."
"argument is assigned to the function when its call."

# 2. In your own words, describe what 
# a conditional statement (if/else) is 

"executes a block of code if a specific condition is met."

# 3. write a simple conditional statement using a comparision operator(greater than, less than, etc. )

in_game_money= 300.00
weapon_in_game= 500.00

if in_game_money > weapon_in_game:
    print('you have the weapons, congrats.')
else:
    print('sorry, insufficient funds.')

# 4. Write a conditional statement for food in the refridgerator.
# your conditional statement should be wrapped in a function that takes one (1)
# parameter. The data type for this parameter should be true or false. 
# If there is food in the refridgerator, print time to cook. If there is 
# NOT food in the fridge, print time to shop. 
# When you call your function there should be an argument that accepts 
# a boolean. 

# keywords = parameter, datatype, print, def, boolean
# we know parameter should be true or false - boolean
# we know we need a function definition and in our definition we need a
# placeholder- parameter. 
# print()

def put_food_in_refridgerator(foood_in_refridgerator):
    if foood_in_refridgerator==True:
        print('time to cook')
    else:
        print('time to shop.')

put_food_in_refridgerator(True)

# 5. Create a function that checks the inventory of cereal for a store. 
# your function should have a parameter that accepts an integer. 
# In your function use a conditional statement to determine if you need 
# to order more cereal. If there is more than 10 boxes, 
# print "inventory full", else if there are less than 
# 10 boxes print "we need to order more cereal".

# keyword = parameter, integer, function, print, conditional statement, inventory,
# comparison using more than

def cereal_inventory(cereal):
    current_cereal_inventory= 10
    if cereal >= current_cereal_inventory:
        print("Inventory is full.")
    else: 
        print("need to order more cereal.")

cereal_inventory(10)