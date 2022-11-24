distancia = float(input('\nQuantos KM tem a sua viagem ? '))

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45

print(f'\n Para sua viagem de {distancia}kms\n Sua passagem custa R${passagem:.2f}')