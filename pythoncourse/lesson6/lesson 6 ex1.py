import random
numberh = int(input('Hi, i am thinking about a number between 0 and 5, try guessing: '))
list = [0, 1, 2, 3, 4, 5]
numberpc = random.choice(list)
print('The number you tried is {}, mine is {}'.format(numberh, numberpc))
if numberh == numberpc:
    print('Congratulations !!!!!!!!')
else:
    print('You are wrong...')
print('---end---')
