n1 = float(input('grade 1: '))
n2 = float(input('grade 2: '))
med = (n1+n2)/2

if med < 5.0:
    print('You failed, your score is {:.2f}'.format(med))
elif 6.9 >= med >= 5.0:
    print('Need to do it again, your score is {:.2f}'.format(med))
else:
    print('approved, your score is {:.2f}'.format(med))
