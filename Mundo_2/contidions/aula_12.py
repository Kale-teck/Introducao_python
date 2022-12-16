nome = str(input('Qual é seu nome ? '))
if nome == 'Kalebe':
    print(f'Que nome bonito !')
elif nome == 'Maria' or nome == 'João' or nome == 'Pedro':
    print('Seu nome é bem popular')
elif nome in 'Ana Jessica Cleide':
    print('Nossa que nome diferente')
else:
    print('Que nome feio')    

print(f'Tenha um bom dia {nome}')