from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hip = hypot(co, ca) #calcula o tamanho da hipotenusa a partir do tamanho dos catetos

print(f'A hipotenusa vai medir {hip:.2f}')
