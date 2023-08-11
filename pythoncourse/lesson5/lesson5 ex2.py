num = int(input('Enter a number between 0 and 9999: '))
u = num // 1 % 10
t = num // 10 % 10
h = num // 100 % 10
th = num // 1000 % 10
print('unity: {}'.format(u))
print('ten: {}'.format(t))
print('hundred: {}'.format(h))
print('thousand: {}'.format(th))
