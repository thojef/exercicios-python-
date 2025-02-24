#Exercício Python 8: Escreva um programa que leia um valor 
#em metros e o exiba convertido em centímetros e milímetros. 

metros = float(input('Digite o tamanho em metros: '))
centimetros = metros * 10
milimetros = metros * 100

print (f'o valor de {metros} M \n'
      f'{centimetros} Cm \n'
      f'{milimetros} Mm. \n'
)
