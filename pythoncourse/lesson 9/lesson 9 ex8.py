frase = str(input('manda a braba: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print(junto, inverso)
if inverso == junto:
    print('Ta certo de tras pra frente de frente pra tras parabens paizao')
else:
    print('nada ver')
print('fimzao')
