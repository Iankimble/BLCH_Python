# WHILE LOOPS- Repeats code indefinitely, while true. 

# Washer and dryer - these machines will repeat - dry sensor
 # while the clothing is not dry, keep drying. 

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