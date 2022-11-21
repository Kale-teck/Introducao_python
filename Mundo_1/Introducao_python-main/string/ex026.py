frase = str(input('Digite uma frase: ')).strip().lower() # strip() pra armazenar já sem espaço

vez = frase.count('a') # count() quantas vezes o argumento aparece
frase = frase.split()
frase = ''.join(frase)

print(f'A letra A aparece {vez} vezes nessa frase')
print(f"A primeira letra A está na posição {frase.find('a') + 1}") # find() encontra o argumento inserido
print(f"A ultima letra A da frase está na posição {frase.rfind('a') + 1}") # rfind começa da reight (direita)