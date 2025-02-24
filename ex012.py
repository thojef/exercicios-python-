# Exercício Python 12: Faça um algoritmo que leia o preço de
# um produto e mostre seu novo preço, com 5% de desconto.

val = float(input('Digite o valor do item: '))
valdesc = val * (1 - 5 / 100)

print (f'O Valor com desconto fica em R${valdesc}')