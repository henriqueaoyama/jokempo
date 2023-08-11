name = str(input('insert your name: ')).strip()

print('Your upper case name is: {}'.format(name.upper()))
print('Your lower case name is: {}'.format(name.lower()))
print('Your name have {} letters'.format(len(name) - name.count(' ')))
divided = name.split()
print('Your first name is {} and have {} letters'.format(divided[0], len(divided[0])))
print('Your last name is {} and have {} letters'.format(divided[1], len(divided[1])))
