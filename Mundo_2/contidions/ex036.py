casa = float(input('Qual valor o valor da casa ? '))
salario = float(input('Qual o seu salário ? '))
anos = int(input('Em quantos anos deseja pagar ? '))

porcentagemLimite = (salario * 30) / 100
prestacao = casa / (anos * 12)

print(f'\nPara pagar uma casa de R${casa:.2f} em {anos} anos\n a prestação será de R${prestacao:.2f}')

if prestacao <= porcentagemLimite:
    print('\nEMPRÉSTIMO CONCEDIDO !')
else:
    print('\nEMPRÉSTIMO NEGADO !')
