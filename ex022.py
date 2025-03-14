'''Exercício Python 22: 
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.
'''

nome = input ('Digite seu nome: ').strip()
print (f'seu nome em maiusculo é: {nome.upper()}.')
print (f'seu nome em minusculas é: {nome.lower()}.')
print (f'seu nome ao todo tem {len(nome) - nome.count (' ')}')
print (f'seu primeiro nome tem {nome.find(' ')} letras')

