import random

n1 = str(input('First student name: '))
n2 = str(input('Second student name: '))
n3 = str(input('Third student name: '))
n4 = str(input('Fourth student name: '))
list = [n1, n2, n3, n4]
random.shuffle(list)

print('the order of presentation will be: {}'.format(list))
