import math
n1 = float(input('Enter the number of adjacent side: '))
n2 = float(input('Enter the number of the opposite side: '))

h1 = math.sqrt(n1**2 + n2**2)

print('The hypotenuse is {:.2f}'.format(h1))
