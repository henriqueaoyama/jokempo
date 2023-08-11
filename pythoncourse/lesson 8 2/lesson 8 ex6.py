n1 = int(input('Enter your age: '))

if n1 <= 9:
    print('Your age is {}, you are MIRIM'.format(n1))
elif 14 >= n1 > 9:
    print('Your age is {}, you are INFANTIL'.format(n1))
elif 19 >= n1 > 14:
    print('Your age is {}, you are JUNIOR'.format(n1))
elif 20 >= n1 > 19:
    print('Your age is {}, you are SENIOR'.format(n1))
else:
    print('Your age is {}, you are MASTER'.format(n1))
