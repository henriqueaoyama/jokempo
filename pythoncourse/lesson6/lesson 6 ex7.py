salary = float(input('How much is your salary? '))
if salary <= 1250:
    print('You will get a 15% raise, now your salary is {:.2f}'.format(salary * 1.15))
else:
    print('You will get a 10% raise, now your salary is {:.2f}'.format(salary * 1.1))
