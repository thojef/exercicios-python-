# Exercício Python 11: Faça um programa que leia a largura e a altura 
# de uma parede em metros,calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma
# área de 2 metros quadrados.

larg = float (input ('Digite a Largura: '))
alt = float (input('Digite a Altura: '))

area = (larg * alt)
tinta = round (area / 2 + 0.20, 2) 

print (f'para pintar uma parede de {area}m², vai precisar de {tinta} litros de tinta')


