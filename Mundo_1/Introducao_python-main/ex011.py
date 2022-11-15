largura = float(input('Qual largura da parede ? '))
altura = float(input('Qual altura da parede ? '))

area_parede = largura*altura
litros_tinta = area_parede/2

print(f'Sua parede tem {largura}x{altura} e ela possui {area_parede}m² e você precisa de {litros_tinta}L de tinta para pintá-la')