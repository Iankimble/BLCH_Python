# Create a function that will multiply each value in the list by 3. 

list_numbers=[1,2,3,4,5,6]

def multiplier():
  list_numbers=[1,2,3,4,5,6]
  for placeholder in list_numbers:
    print(placeholder+10)

# multiplier()

a = 100
b = 20

if b > a:
  print('b is greater than a')
else:
  print('b is less than a')

# Above 75
# belov 70 is cool
# right in the middle is perfect

def check_weather():
  temp = float(input('what is the temperarture'))
  if temp > 75:
    print('its hot')
  elif temp < 70:
    print('it is cold')
  else:
    print('its perfect.')

check_weather()