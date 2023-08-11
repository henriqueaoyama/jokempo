import math
n1 = float(input('Enter the number of adjacent side: '))
n2 = float(input('Enter the number of the opposite side: '))

h1 = math.hypot(n1, n2)

print('The hypotenuse is {:.2f}'.format(h1))
