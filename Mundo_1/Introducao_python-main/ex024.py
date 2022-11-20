cidade = str(input('Digite o nome de uma cidade: '))

santo = cidade.strip() # elimina espaços beginner and end por precaução
santo = santo.split() # Quarda nome e sobrenome em objetos distintos
santo = santo[0].lower() # caixa baixa pra facilitar busca

if 'santo' in santo: # testa se existe a palavra na string digitada
    print(f'\n{cidade} começa com a palavra {santo.title()}\n')
    # se sim, o método title() retorna a letra inicial para maiúscula
else:
    print(f'\n{cidade} não começa com a palavra (Santo)\n')
    