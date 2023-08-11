prod = int(input('What is the price?: '))
print('''PAYMENT METHODS
[ 1 ] All money
[ 2 ] All card
[ 3 ] 2x card
[ 4 ] 3x or more card
''')
opt = int(input('Select your option: '))

if opt == 1:
    print('Your final cost will be {}'.format(prod * 0.9))
elif opt == 2:
    print('Your final cost will be {}'.format(prod * 0.95))
elif opt == 3:
    print('Your final cost will be {}'.format(prod))
elif opt == 4:
    print('Your final cost will be {}'.format(prod * 1.2))
else:
    print('ERROR')
