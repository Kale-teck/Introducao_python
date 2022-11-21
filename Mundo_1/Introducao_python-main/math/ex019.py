from random import choice
n1 = str(input('Nome do primeiro Aluno: '))
n2 = str(input('Nome do segundo Aluno: '))
n3 = str(input('Nome do terceiro Aluno: '))
n4 = str(input('Nome do quarto Aluno: '))

lista_alunos = [n1, n2, n3, n4]

escolhido = choice(lista_alunos)

print(f'O aluno escolhido foi {escolhido}')