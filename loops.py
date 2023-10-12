# the colon symbol after a function typically denotes that 
# code instruction will follow. 

  # while loop = repeat some code forever, 
  # unitl the condition its looking is met.  

# simple loop
i=0
while i <= 10: 
    print(i) # instruction 1
    print(i==i) # instruction 2
    i+=4 # instruction 3

variable= False
while variable == True:
    print('this will run infinitly')

# def exampleFunction(parameter):
    # run these instructions
     
# if 0 > 1:
    # run these instructions
# else:
    # run these instructions

# elif:
    # run these instructions

# while 0 > 1:
    # run these instructions

def enter_userName():
    user_name= input('whats your username? ')
    while user_name !='ian': # while user name is not the same
        print('incorrect please enter your name ')
    user_name= input('whats your username? ')
    print('welcome ian')

car='mazda'
exlist2=[1,2,3,4,5,6,7]
exList= [True,
         1, 10.0, 
         'strings',
         exlist2,
         car
        ]

groceryList= ['milk',
              'fruit',
              'ground beef',
              'string beans',
              'trash bags']

print(len(groceryList))

i=0
while i < len(groceryList):
    print(groceryList[i])
    i+=1