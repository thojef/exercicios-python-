#Exercício Python 9: Faça um programa que leia um número 
#Inteiro qualquer e mostre na tela a sua tabuada.

#Forma 1
num = int(input('Digite um numero: '))

print (num,'x 2 = ', num*2)
print (num,'x 3 = ', num*3)
print (num,'x 4 = ', num*4)
print (num,'x 5 = ', num*5)
print (num,'x 6 = ', num*6)
print (num,'x 7 = ', num*7)
print (num,'x 8 = ', num*8)
print (num,'x 9 = ', num*9)
print (num,'x 10 = ', num*10)

#Forma 2
numb = int(input('Digite algum numero: '))

for i in range(0, 10):
    print(f'{numb} x {i} = {numb * i}')



