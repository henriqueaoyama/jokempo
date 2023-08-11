name = str(input('What is your name? ').strip())
name1 = name.split()
print('Your first name is {}'.format(name1[0]))
print('Your last name is {}'.format(name1[len(name1)-1]))
