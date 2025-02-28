#Exercício Python 16: Crie um programa que leia um número 
# Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# forma 1
num = float(input('Digite um numero Real: '))
print (f'a parte inteira do numero {num} é {int(num)}')

# forma 2
import math
n = float(input('Digite um numero Real: '))
print (f'a parte inteira de {n} é {math.trunc(n)}')


