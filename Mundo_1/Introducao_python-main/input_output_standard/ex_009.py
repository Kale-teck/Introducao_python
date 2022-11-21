from ast import For


n = int(input('Digite um número : '))

for x in range(10):
   print('{} * {} = {}'.format(n, x+1, n*(x+1)))
   x+1