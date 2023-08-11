n1 = int(input('enter number: '))
n2 = int(input('enter number: '))
n3 = int(input('enter number: '))
if n2 < n1 + n3 and n1 < n2 + n3 and n3 < n1 + n2:
    print('Can form a triangle')
    if n1 == n2 == n3:
        print('Equilatero')
    elif n1 != n2 != n3 != n1:
        print('Escaleno')
    else:
        print('Isoceles')
else:
    print('Cannot form a triangle')
