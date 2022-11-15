kms = float(input('Quantos kms você rodou com o carro? '))
dia = int(input('Quantos dias você passou com o carro? '))

valor = (dia*60) + (kms*0.15)

print(f'O total a pagar é R${valor:.2f}')