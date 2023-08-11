frase = 'hello world'
print(frase[6:11])
print(frase[:5])
print(frase[6:])
print(len(frase))
print(frase.count('l'))
print(frase.find('wor'))
print('hello' in frase)
print(frase.replace('world', 'my friend'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase.split()
print(frase.split(), '-'.join(frase))


frase2 = '   mamaco gago  '
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())
