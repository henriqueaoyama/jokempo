from random import randint
from time import sleep
numberh = int(input('Hi, i am thinking about a number between 0 and 5, try guessing: '))
numberpc = randint(0, 5)
print('PROCESSING...')
sleep(3)
print('The number you tried is {}, mine is {}'.format(numberh, numberpc))
if numberh == numberpc:
    print('Congratulations !!!!!!!!')
else:
    print('You are wrong...')
print('---end---')
