# simple loop
i=0
while i <= 10:
    print(i)
    i+=1


# looping over numbers incrementally until it gets to 6. 
def check_for_number():
    repeater = 1
    
    while repeater <6:
        print('looking for number 6. this program will stop at 6')
        repeater +=1
    
    if repeater==6:
        print('found the number 6')

check_for_number()

# loop that checks if a password is correct
def check_password():
    iterator= 1
    password = 'open'
    
    while iterator <= 3:
        userInput= input('please type in your password')
        if userInput !=password:
            print('try again')
        else:
            print('welcome, you are logged in.')
            break
        iterator +=1

        if iterator > 3:
            print('too many attempts, try agian later.')

#check_password()

