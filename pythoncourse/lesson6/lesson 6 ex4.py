km = int(input('How far you will go? '))
if km <= 200:
    print('Your trip will cost {} dollars'.format(km * 0.5))
else:
    print('Your trip will cost {} dollars'.format(km * 0.45))
print('Have a nice trip')
print('---end---')
