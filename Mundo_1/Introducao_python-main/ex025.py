nome = str(input('Digite seu nome completo: '))

silva = nome.lower()
silva = silva.strip()
silva = silva.split()

if 'silva' in silva:
    print(f'\nO nome {nome} possui possui a palavra (Silva)\n')
else:
    print(f'\nO nome {nome} NÃO possui a palavra (Silva)\n')