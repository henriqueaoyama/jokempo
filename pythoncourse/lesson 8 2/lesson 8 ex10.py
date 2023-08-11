from random import randint
items = ('ROCK', 'PAPER', 'SCISSOR')
comp = randint(0, 2)
print('-----JOKENPO-----')
print('''Choose your option: 
[ 0 ] ROCK
[ 1 ] PAPER
[ 2 ] SCISSOR
''')
opt = int(input('Choose: '))
print('PC chose {}'.format(items[comp]))
print('You has chosen {}'.format(items[opt]))
if comp == 0: #PC chose ROCK
    if opt == 0:
        print('TIE')
    elif opt == 1:
        print('YOU WON')
    elif opt == 2:
        print('PC WON')

elif comp == 1: #PC chose PAPER
    if opt == 0:
        print('PC WON')
    elif opt == 1:
        print('TIE')
    elif opt == 2:
        print('You WON')

elif comp == 2: #PC chose SCISSOR
    if opt == 0:
        print('YOU WON')
    elif opt == 1:
        print('PC WON')
    elif opt == 2:
        print('TIE')
