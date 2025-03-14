# Exercício Python 25: Crie um programa que leia o nome de
# uma pessoa e diga se ela tem “SILVA” no nome.

nome = input ('Digite o nome completo: ').strip()
print (f'o seu nome tem Silva ? {'SILVA' in nome.upper()}')
    