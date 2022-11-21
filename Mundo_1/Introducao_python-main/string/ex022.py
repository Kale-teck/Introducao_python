nome = str(input('Digite seu nome completo: ')) # entrada do nome do usuário

nome_sem_espacos = nome.strip() # elimina espaços em branco (beginner and end)
nome_sem_espacos = nome_sem_espacos.split() # separa cada palavra
nome_sem_espacos = ''.join(nome_sem_espacos) # junta cada palavra sem espaço

print(f'''      Seu nome em minúsculas é: {nome.lower()}
      Seu nome em maiúsculas é: {nome.upper()}
      Seu nome possui {len(nome_sem_espacos)} letras
      Seu primeiro nome tem {len(nome.split()[0])} letras''') #optei por otimizar separando os nomes e lendo o tamanho len(do primeiro nome[0] dentro do print)