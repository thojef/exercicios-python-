#Exercício Python 23: Faça um programa que leia um número de
#0 a 9999 e mostre na tela cada um dos dígitos separados.

print('Sistema que fragmenta casas decimais de um numero intgeiro!')
num = int (input('Informe um numero: '))
n = str(num).zfill(4)

print (f'Fragmentando o numero {num}')
print (f'Unidade: {n[3]}')
print (f'Dezena: {n[2]}')
print (f'Centena: {n[1]}')
print (f'Milhar: {n[0]}')
