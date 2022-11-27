# entrada de 3 valores e exibir maior e menor

i = 0
valores = [] # declaração da lista vazia
while i < 3: # repetir input 3 vezes
    valor = int(input('\nDigite qualquer valor : '))
    valores.append(valor) # adiciona o input na lista
    i += 1 # incrementa o contador
print(f'\n O maior valor digitado foi {max(valores)}') # maior
print(f'\n O menor valor digitado foi {min(valores)}') # menor