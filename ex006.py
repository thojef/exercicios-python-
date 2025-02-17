# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# forma 1

n = int (input ('digite um valor: '))
dobro = n * 2
triplo = n * 3
raiz = n ** 0.5

print (f'{n}. \n'
       f'dobro: {dobro}. \n'
       f'Triplo: {triplo}. \n'
       f'raiz quadrada: {raiz}.')

# forma 2
import math

n = int(input('Digite um numero: '))
print (f'Numero: {n}. \n'
       f'Dobro: {n * 2}. \n'
       f'Triplo: {n * 3}. \n'
       f'Raiz quadrada:{math.sqrt (n)} ')
