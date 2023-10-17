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

# Printer Loop


# Stop Light Loop 

