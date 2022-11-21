from random import randint

numero = int(input('Digite um número: '))

aleatorio = randint(0, 5)

if numero == aleatorio:
    print(f'\nVocê VENCEU ! {numero} é igual a {aleatorio} !')
else:
    print(f'\nVocê PERDEU ! {numero} é diferente de {aleatorio} ! :( ')
    