# while loop
# iterator
#while i < 6: # condition/ scenario we want to check for
#  print(i) # instruction on what to do next 
 # increment - the number of times we want to do it. 
#i += 1

# conditional statement
def password_code():
    actual_password='blch'
    user_password_attempt= input("please enter a password: ")
    attempt = 0
    while attempt > 3:
        while user_password_attempt != actual_password :
                print('password is ncorrect. Please enter the passcode.')
                print('you have ' + attempt + 's left.') 
    attempt +=1
    
    print('password is correct, you may enter.')



password_code()