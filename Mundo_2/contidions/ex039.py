from datetime import date

ano_nasceu = int(input('\nQual o ano do seu nascimento ? '))

ano_atual = date.today().year
idade = ano_atual - ano_nasceu
ano_alistamento = ano_atual - (idade - 18)
previsao_ano = ano_atual + (18 - idade)

print(f'\nQuem nasceu em {ano_nasceu} tem {idade} anos em {ano_atual}.')

if idade > 18:
    print(f'\nO seu alistamento já devia ter sido feito há {idade - 18} anos.\nSeu alistamento foi em {ano_alistamento}\n')
elif idade == 18:
    print(f'\nVocê tem que se alista IMEDIATAMENTE !\n')
else:
    print(f'\nAinda faltam {18 - idade} anos para o alistamento.\nSeu alistamento será em {previsao_ano}\n')
