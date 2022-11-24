velocidade = float(input('Qual a velocidade do seu carro em Km? '))

if velocidade <= 80:
    print(f'\n Tenha um bom dia! Dirija com segurança !')
else:
    multa = (velocidade-80)*7
    print(f'\n MULTADO você excedeu o limite de 80km/h \n Você pagará multa de R${multa} !!! ')