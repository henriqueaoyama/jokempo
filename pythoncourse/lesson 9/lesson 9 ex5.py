soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('(os números ímpares vão ser desconsiderados) Coloca um numero ai {} paizao: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Seus {} números pares somaram e formaram {}'.format(cont, soma))
