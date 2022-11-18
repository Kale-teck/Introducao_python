from random import shuffle
n1 = str(input('Nome do primeiro Aluno: '))
n2 = str(input('Nome do segundo Aluno: '))
n3 = str(input('Nome do terceiro Aluno: '))
n4 = str(input('Nome do quarto Aluno: '))

lista_alunos = [n1, n2, n3, n4]
shuffle(lista_alunos)

print(f'\n A ordem selecionada foi \n {lista_alunos}')