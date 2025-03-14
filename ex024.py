# Exercício Python 24: Crie um programa que leia o nome 
# de uma cidade diga se ela começa ou não com o nome “SANTO”.

name = input ('Digite o nome de uma Cidade: ').strip()
print(name[:5].upper() == 'SANTO')

