preco = float(input('Qual é o preço do produto? R$'))

print(f'Seu produto custava R${preco:.2f}, na promoção com 5% de desconto fica: R${preco-(preco*5/100):.2f}')