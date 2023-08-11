hv = float(input('Whats is the value of the house? '))
salary = float(input('How much is your salary? '))
time = int(input('How many years will you take to pay? '))
month = time*12

print("""You will pay {:.2f} dollars for month during {} months 
and your salary 30% is {:.2f}""".format(hv/month, month, salary*0.3))

print('You will pay {:.2f} dollars for month during {} months '.format(hv/month, month), end='')
print('and your salary 30% is {:.2f}'.format(salary*0.3))

if hv/month >= salary*0.3:
    print('Your loan is denied')
else:
    print('Your loan is allowed')
