weight = float(input('Enter your weight: '))
height = float(input('Enter your height in m: '))

IMC = weight / height**2

if IMC <= 18.5:
    print('IMC is {:.2f}: Below'.format(IMC))
elif IMC <= 25:
    print('IMC is {:.2f}: Right'.format(IMC))
elif IMC <= 30:
    print('IMC is {:.2f}: Above'.format(IMC))
elif IMC <= 30:
    print('IMC is {:.2f}: Obesity'.format(IMC))
else:
    print('IMC is {:.2f}: Super Obesity'.format(IMC))
