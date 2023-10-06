# Create a function that will inform a user if the 
# weather is hot or cold based on a argument passed into it.
# The data being passed needs to be a float number. In your function,
# if the temperature is over 75.00 return to the user it is hot outside and if 
#it is below 70 it is cold. If it is neither above 75 but not below 70 return a
# message saying the weather is perfect. 


def weather(temp):
    temp=float(input('what is the temperature outside? '))
    if temp < 70.00:
        print('it is cold outside')
    elif temp > 75.00:
        print('it is warm outside')
    else:
        print('its perfect.')

# weather(temp)

# Create a function that will multiply each value in the list by 3. 

list_numbers=[1,2,3,4,5,6]

#for x in list_numbers:
#    print(x+10) 

# create a simple conditional statement

#condition = input('do you have a pet? ')

#if condition=='yes':
#    print('i hope you enjoy having a pet.')
#elif condition=='no':
#    print('you should get one. They are nice to have in hard times. ')
#else:
#    print('please enter either yes or no')


# Create a function that uses conditional statements that will evaluate the data types 
# of the value being passed into a function by a user. When the user enters a data type,
#  the function should return a message telling the user what the data type is. 

# Ex. message that should be returned: “you have entered an integer”



ricardos_list=['chicken','pizza','water']
def list_main(ricardos_list):
    if datatype=='string':
        print('you have entered a string')
    elif datatype=='integer':
        print('you have entered an integer')
    else:
        print('you have a boolean')
    


def datatype():
    user_input= input('input a data type')
    hi=type(user_input)
    if hi == str(user_input):
        print('this is a string')
    elif hi== int(user_input):
        print('this is a integer')
    else:
        print('please enter number/phrase that represents data type')



var= input('type somthing')
print(var)

if type(var)== str:
    print('this is a string')

elif type(var)== int:
    print('this is an integer')