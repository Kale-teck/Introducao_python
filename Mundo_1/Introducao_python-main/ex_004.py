a = input('Digite algo  ')
print('O tipo primitivo desse valor é ', type(a)) #sempre será str por causa do input
#neste caso abaixo a é um objeto
print('só tem espaços? ', a.isspace())
print('É um  número? ', a.isnumeric())
print('É alfabético ?', a.isalpha()) #esses is...etc são métodos python
print('É alfanumérico ?', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle()) #para maiúsculas e minúsculas juntas

