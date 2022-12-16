numero = int(input('Digite um número inteiro qualquer : '))

def base():
    print('\nInforme qual conversão deseja fazer')
    print(' [1] para binário')
    print(' [2] para octal')
    print(' [3] para hexadecimal')
    return int(input(' '))

base = base()

if base == 1:
    print(f'{numero} convertido para binário é {bin(numero) [2:]}')
elif base == 2:
    print(f'{numero} convertido para octal é {oct(numero) [2:]}')
elif base == 3:
    print(f'{numero} convertido para hexadecimal é {hex(numero) [2:]}')
else:
    print('Opção inválida !')
