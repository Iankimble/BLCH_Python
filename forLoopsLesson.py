# WARM UP -10/ 20/ 2023

# Time- 30 minutes

# Go to the following link, read and practice the code 
# examples on For loops.

link='https://www.programiz.com/python-programming/for-loop'


# Arrays 
listTwo=[1,2,3,4,5,6]
exampleList=['word',1, 1.0, False, listTwo]

# While Loops = Run indefinitley, so long as a condition is true

# For Loops = Run up to the number of items in an array. 
def vehicleLoop():
    list_of_vehicles= ['cars','boats','planes','submarines','train']

    for place_holder_Iterator_vehicle in list_of_vehicles:
        print(place_holder_Iterator_vehicle)
        if place_holder_Iterator_vehicle == 'planes':
            break

# iterate with a FOR loop
def forloopFunction():
    for x in range(6): 
        print(x)

# iterate with a WHILE loop
def whileLoopFunction():
    x= 0
    while x <= 6:
        print(x)
        x+=1

dante=['Dante',18,'left hand']
mark=['Mark',16,'right hand']
bill=['Bill',19,'left handed']
sarah=['Sarah',15,'ambedextrous']

studentDrivers=[dante,mark,bill,sarah]

print(studentDrivers)

for drivers in studentDrivers:
    if drivers[3] == 'left hand':
        print(drivers[0] + 'is left handed.')
        #print(drivers[0] + ' cannot get liscense.')




# WHILE Loop - Is a keyword that will repeat a block of code 
# indefinitly, so long as the condition is true.  

# FOR Loop - Is a key that will repeat a block of code,
# but only to the limit of the array/list. 
# THIS DOES NOT RUN INDEFINITELY. 

zoo= ['tiger','bear','eagle','otter','dolphin']
exampleList2=['word',10,11.1212, True, zoo]

var='ian'
num=2332

profile= [ name='Ian',
          age=32,
          career='engineer'
          city='Philly'
          canDrive=True,
]

profile= [ name='Alex',
          age=23,
          career='contractor'
          city='Baltimore'
          canDrive=True,
]
     