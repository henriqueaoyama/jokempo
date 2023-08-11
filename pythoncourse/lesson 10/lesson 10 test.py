#c = 1
#while c < 10:
#    print(c)
#    c = c + 1
#print('fim')
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('o total de numeros pares digitados foi de {} e o total de numeros impares foi de {}'.format(par, impar))
