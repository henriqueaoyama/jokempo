name = str(input('What is your name? '))
colors = {'clean': '\033[m',
          'blue': '\033[34m',
          'red': '\033[31m',
          'yellow': '\033[33m',
          'blacknwhite': '\033[7;37m'}
print('Hello {}{}{}, nice to meet you !!!'.format(colors['red'], name, colors['clean']))
print('Hello {}{}{}, nice to meet you !!!'.format(colors['blue'], name, colors['clean']))
print('Hello {}{}{}, nice to meet you !!!'.format(colors['yellow'], name, colors['clean']))
print('Hello {}{}{}, nice to meet you !!!'.format(colors['blacknwhite'], name, colors['clean']))
