num = int(input('Please input a number: '))
print('''Choose one of the below options of conversion:
[ 1 ] to binary
[ 2 ] to oct
[ 3 ] to hexa''')
option = int(input('Your option: '))

if option == 1:
    print('{} converted to binary is {}'.format(num, bin(num)[2:]))
elif option == 2:
    print('{} converted to oct is {}'.format(num, oct(num)[2:]))
elif option == 3:
    print('{} converted to hexa is {}'.format(num, hex(num)[2:]))
else:
    print('ERROR')
