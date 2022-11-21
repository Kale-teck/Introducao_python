salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario*15/100
novo_salario = salario + aumento
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novo_salario:.2f}')