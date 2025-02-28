# 13: Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

colaborador = input ('Digitte o nome do Colaborador: ')
salario =  float (input ('Digite o valor do Salario do Colaborador: '))

aumento = round ( salario * (1 + 15 / 100), 1 )

print (f'Salario atual de {colaborador}: R${salario}.')
print (f'Novo salario de {colaborador} com ajuste de 15%: R${aumento}')
