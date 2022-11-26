#dizer se um ano é bissexto ou não

from datetime import date

ano = int(input('\nInforme um ano (0 para saber o ano atual): '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0):
    print(f'\nO ano {ano} é bissexto !\n')
else:
    print(f'\nO ano {ano} NÃO é bissexto !\n')

