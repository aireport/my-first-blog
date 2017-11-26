print('Hello, Django girls!')
if 5>2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')

def hi(name):
    #name = 'Sonja'
    if name == 'Ola':
        print('Hey Ola')
    elif name == 'Sonja':
        print('Hey Sonja')
    else:
        print('Hey anonymous!')
#hi()
hi("Ola")

def hi(name):
    print('Hi ' + name + '!')
hi("Rachel")
