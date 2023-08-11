n1 = int(input('enter number: '))
n2 = int(input('enter number: '))
n3 = int(input('enter number: '))
smaller = n1
if n2 < n1 and n2 < n3:
    smaller = n2
if n3 < n1 and n3 < n2:
    smaller = n3

larger = n1
if n2 > n1 and n2 > n3:
    larger = n2
if n3 > n1 and n3 > n2:
    larger = n3
print('The smaller number is {}'.format(smaller))
print('The larger number is {}'.format(larger))
