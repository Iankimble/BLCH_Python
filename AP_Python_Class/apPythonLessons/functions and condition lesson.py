# create a function that will be used for a user's profile. This function
# should accept 3 arguments; a picture, name, location. when the code is ran,
# it should print out these values. 

# we know we need to use picture, name, location
# we know we need to print it out at some point.  

def profileData():
    location = input('where are you from?')
    name = input('whats your name?')
    picture= input('upload a picture')
    
    print('success! heres your profile info')
    print("name- " + name)
    print("location- "+ location)
    print("picture: "+ picture)

# profileData()


# conditional statements
#Conditional Statements are a tool that allows 
# programmers to control the outcome/ execution of a program 
# depending on the scenario. We use  the if and else keywords 
#  to execute a conditional statement

sunIsOut = False

if sunIsOut == True:
    print('its day time.')
else:  
    print('night time') 

weekday= True

if weekday == True:
    print('you have school.')
else:
    print("no school.")


def buyOf2K(moneyInAccount):
    priceOfGame= 70.00
    if moneyInAccount >= priceOfGame:
        print('you got game!')
    else:
        print('you aint got no game.')

#buyOf2K(70.00)