# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome_completo = str(input('Digite o nome completo: ')).strip()
nome = nome_completo.split()
nome_de_cadastro = nome[0] + ' ' + nome[len(nome)-1]
print(f'Nome de Cadastro: {nome_de_cadastro}.')


