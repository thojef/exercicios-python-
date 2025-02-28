# Exercício Python 19: Um professor quer sortear um dos seus 
# quatro alunos para apagar o quadro. Faça um programa que ajude 
# ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

lista_alunos = []
while True:
    nomes = input('Digite o nome dos alunos para adicionar a lista: ')
    if nomes.lower() == 'sair':
        break
    lista_alunos.append(nomes)

sorteado = random.choice(lista_alunos)
print(f'O aluno escolhido foi {sorteado}!')

