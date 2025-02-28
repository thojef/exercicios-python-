# 
# Exercício Python 17: Faça um programa que leia o comprimento do 
# cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

# forma 1
ca = float(input('Digite o tamanho do Cateto: '))
co = float(input('Digite o tamanho do cateto oposto'))
hi = (ca ** 2 + co ** 2) ** 0.5
print (f'o valor da hipotenusa é: {hi}')

# forma 2
import math

cat = float(input('Digite o tamanho do Cateto: '))
cop = float(input('Digite o tamanho do cateto oposto'))
hip = math.hypot (cat,cop)
print (f'o valor da hipotenusa é: {hip}')
