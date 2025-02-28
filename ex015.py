# Exercício Python 15: Escreva um programa que pergunte a quantidade 
# de Km percorridos por um carro alugado e a quantidade de dias 
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que 
# o carro custa R$60 por dia e R$0,15 por Km rodado.

kilometragem = int (input('Quantidade de kilometros percorridos: '))
diaria = int (input('quantidade de dias ultilizados: '))

valor_kilometros = round ( kilometragem * 0.15, 2)
valor_diaria = round ( diaria * 60, 2)

print (f'valor a pagar dos kms rodados: R${valor_kilometros} ')
print (f'valor a pagar dos Dias: R${valor_diaria}')

valor_total = valor_kilometros + valor_diaria

print (f'valor total a pagar é R${valor_total} ')