numero = int(input('Digite um número: '))

if numero >= 0 and numero <= 9999:
    numero_str = str(numero) # conversão para string para navegar pelos indíces da lista
    print(f'Unidade: {numero_str[-1]}')
    if numero >= 10: # os testes continuam no inteiro  digitado pelo usuário
        print(f'Dezena: {numero_str[-2]}') # porém as casas decimais são melhor localizadas assim
    if numero > 100:
        print(f'Centena: {numero_str[-3]}')
    if numero >= 1000:
        print(f'Milhar: {numero_str[-4]}')