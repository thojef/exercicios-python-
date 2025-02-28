# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de
# apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos 
# quatro alunos e mostre a ordem sorteada.

import random

lista_alunos = []
while True:
    alunos = input('Digite o nome dos alunos par adicionar na lista (ou ''sair'' para sair): ')
    if alunos.lower() == 'sair':
        break
    lista_alunos.append (alunos)

random.shuffle(lista_alunos)
print(f'A ordem de apresentaçao será: {lista_alunos}')
    