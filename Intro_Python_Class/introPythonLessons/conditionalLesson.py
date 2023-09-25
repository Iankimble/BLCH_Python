def isClassOver(timeParameter):
    if timeParameter>11.30:
        print('class is over. Time to go.')
    else:
        print('no, lets keep going')

isClassOver(11.31)

def writeName(nameParameter):
    user_name= input('what is your name?')
    if not isinstance(nameParameter, (int, float)): 
        print('cannot be a number')
    else:
        print('hello ' + user_name)

#writeName('Ian')

def petNoise(petParameter):
    if petParameter== 'dog':
        print('woof woof')
    elif petParameter =='cat':
        print('meow')

#petNoise('cat')

