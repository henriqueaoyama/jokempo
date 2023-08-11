speed = int(input('ticket simulator, how fast were you? '))
km = (speed - 80)
price = (km * 7)
print('the speed limit of this road was 80km/h, you were {}'.format(speed))
if speed > 80:
    print('your ticket will cost {} dollars since you were {}km/h faster than the limit'.format(price, km))
else:
    print('all good, driving correctly')
print('---end---')
