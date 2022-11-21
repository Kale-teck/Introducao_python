nome = str(input('Digite seu nome completo: ')).title().strip()

print(f'\nPrazer em te conhecer {nome} !')

nome = nome.split()

print(f'\nSeu primeiro nome é {nome[0]}')
print(f'\nSeu último nome é {nome[-1]}\n')