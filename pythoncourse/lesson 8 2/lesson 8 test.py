name = str(input('Hello, what is you name? ')).strip()
name1 = name.upper()
if name1 == 'HENRIQUE':
    print('What a beautiful name')
elif name1 == 'MARIA' or name1 == 'PAULO' or name1 == 'JANETE':
    print('You are an asshole')
elif name1 in 'ANA BRUNA DANIELE JULIANA':
    print('Bagayaya girls')
else:
    print('Your name is common')
print('Have a good day, {}'.format(name))
