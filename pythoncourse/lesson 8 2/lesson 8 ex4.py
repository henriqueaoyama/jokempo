year = int(input('Year of birth: '))
age = 2022 - year
if age < 18:
    print('Still have time until your military suffer, {} years'.format(18-age))
elif age == 18:
    print('Time for your military suffer')
else:
    print('Your military suffer ended in {}'.format(2022-(age-18)))
