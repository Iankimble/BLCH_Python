# WHILE LOOPS- Repeats code indefinitely, while true. 


# create a new python file called loopReviewActivity.py.

# WARM UP 20 MINS
# Washer and dryer 
# create a while loop for a washer and dryer program. 
# your loop should check to see if the clothes are dry. If the clothes are not
# dry, the loop should keep going. If they are dry the loop will stop.
# use what you learned in class to solve this prompt. There are multiple ways
# to approach this. 

washer_timer= int(i  nput('How long do you want to wash your clothes?: '))
while washer_timer > 0:
    print('clothes are still washing')
    washer_timer-=1
print('clothes are washed.')
















# Security cams - sensor- while the sensor is running; stay silent, 
# otherwise if it does detect somthing sound the alarm. 

# Refridgerator- while door is closed; keep the light off. 
# Once the door opens the light turns on. 



# 1. Ring Cam While Loop 
# while camera is running, do nothing- but when it detects a person, ring alarm.

# variable represent number of people in cameras sight
def cameraSensor():
    cameraView = 0
    while cameraView < 1: 
        print("No one in sight.")
        sightSensor =input('Is there anyone in sight? Enter y for yes and n for no.')
        if sightSensor =='y':
            print('ALARM!!!!')
            break

# 2. Dryer While Loop- sensor running while clothes are not dry.

def dryClothingSensor():
    areClothesDry = False
    while areClothesDry == False:
        print('keep drying clothes')
        dryClothingSensor = input('are the clothes dry? Enter y for yes, n for no ') 
        if dryClothingSensor == 'y':
            print(' stop the dryer. Clothes are dry') 
            break

dryClothingSensor()

# 3. Outdoor Light While Loop


# While Loop - a function that will 
# run set of code instructions(statements),
# While the condition is true, indefinitely.  


# Passcode Loop 

# Printer Loop

# Stop Light Loop 

def passcode_attempt_logic():
    passcode = 1234
    passcodeAttempt_Count= 0 

    while passcodeAttempt_Count < 4:
        passcode_Attempt = int(input('please enter the passcode: '))
        if passcode_Attempt != passcode: 
            print('Incorrect passcode. Try again. ')
        else: 
            print("correct! you may enter! ")
            break
        passcodeAttempt_Count +=1

passcode_attempt_logic()


# Create a loop that will act as a sensor for a lighting system.
# If there are objects in the lights view; turn the light on, Otherwise
# the light should always be off in the loop. 

# Bonus: Right a condition for when it 
# reaches a certain number the lights automatically switch to on. This number should
# represent time.  

# 3. Outdoor Light While Loop

# While Loop - a function that will 
# run set of code instructions(statements),
# While the condition is true, indefinitely.  

# Write a loop that will work for these three scenarios

# Passcode Loop- write a program that will check 
# if a passcode is correct. While the passcode is not correct; 
# Ask the user to try again. User gets 4 attempts. 

# Printer Loop

# Stop Light Loop 

