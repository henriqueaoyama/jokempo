n1 = int(input('value of n1: '))
n2 = int(input('value of n2: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
id = n1 // n2
e = n1 ** n2

print('the sum is: {} \nthe multiplication is: {} \nthe division is: {:.3f}'.format(s, m, d))
print('the integer division is: {} \nthe exponential is: {}'.format(id, e))
