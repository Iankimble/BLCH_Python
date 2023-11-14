tempMax= 90
tempMin= 10
currentTemp= 80

#Fridge Logic
# user should be able to select which function they want to call and fix. 
def fridgeMainInterface():
    print('Hello Human! How can I help you today? Please select which option youd like to use?')
    print('select 1 for water and ice dispenser. ')
    print('select 2 for refidgerator temperature. ')
    print('select 3 to check the expiration dates on your food. ')
    print('select 4 to exit the refiderator settings. ')
    user_input=int(input('Please enter the number for the feature youd like to access: '))
    while user_input < 5:
        if user_input == 1:
            water_ice_dispenser()
        elif user_input == 2:
            fridge_temperature()
        elif user_input == 3:
                food_expiration_sensor()
        elif user_input == 4:
            print('Exiting settings. Have a great day!')
            break
    else:
        print('_______________________________________________________')
        print('Sorry, I dont understand your request. Please enter a valid request.')
        fridgeMainInterface()

# Find the errors and fix ice and water dispenser

def water_ice_dispenser():
# user should be able to choose between water or ice
    user_Selection = input('Hello, would you like water or ice?: Please enter 1 for water and 2 for ice. If you are finished type in the letter e. ')
    if user_Selection == str(1):
        cups_of_water = input('How many cups of water would you like? please provide a number between 1-5 ')
        cups_of_water=100
        print('Heres your water! : '+ str(cups_of_water))
    elif user_Selection == str(2):
        ice_cubes= str(input('How many ice cubes would you like? Please enter a number for your ice cubes: '))
        print('you have ' + ice_cubes +' ice cubes. Enjoy') 
        print('Heres your ice cubes! : '+str(ice_cubes))
    elif user_Selection == 'e':
        print('Have a nice day. Comeback when youre thirsty.')
        fridgeMainInterface()    

# if the select water they should be asked how many cups of water they would like
# if they select ice they should be asked how many cubs of ice would they like 

# Fix fridge temperature
def fridge_temperature():

    while currentTemp < tempMax:
        userRes=('would you like to increase or decrease the temperature? please enter i for ncrease and d for decrease.')
        if userRes=='i':
            currentTemp=+1
        elif userRes=='d':
            currentTemp=-1
    else: 
        confirm = input('would you like to return to the settings main menu? enter y for yes and n for no. ')
        if confirm =='y':
            fridgeMainInterface()
        else:
            fridge_temperature()
        
# user should be able to enter a value that will increment and decrement the temperature on a loop
# when the user is done they can enter done to exit the loop.   

# Fix expiration sensor
def food_expiration_sensor():
        print('logic coming')


fridgeMainInterface()

