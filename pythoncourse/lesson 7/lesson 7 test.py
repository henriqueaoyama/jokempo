n1 = int(input('enter number: '))
n2 = int(input('enter number: '))
n3 = int(input('enter number: '))
if n2 < n1 + n3 and n1 < n2 + n3 and n3 < n1 + n2:
    print('\033[32;40mCan form a triangle\033[m')
else:
    print('\033[31;40mCannot form a triangle\033[m')
