# Exercício Python 18: Faça um programa que leia um ângulo qualquer 
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print(f'o angulo {angulo} tem o seno de: {seno:.4f}')

cosseno = math.cos(math.radians(angulo))
print(f'o angulo {angulo} tem o cosseno de: {cosseno:.4f} ')

tangente = math.tan(math.radians(angulo))
print(f'o angulo {angulo} tem a tangende de: {tangente:.4f}')
