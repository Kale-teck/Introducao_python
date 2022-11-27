salario = float(input('\nQual o salário do funcionário ? R$'))

if salario >= 1250.00:
    reajuste = salario + salario * 10 / 100
else:
    reajuste = salario + salario * 15 / 100

print(f'\nQuem ganhava R${salario:.2f} passa a ganhar R${reajuste:.2f} agora.')