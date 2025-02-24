#Exercício Python 10: Crie um programa que leia quanto dinheiro uma
#pessoa tem na carteira e mostre quantos dólares ela pode comprar.

# Forma 1

val = float (input ('Digite qual valor tem disponivel: '))
dol = float (input ('Digite o valor do dolar hoje: '))

# aqui o cambio e troco servem de parametros, mas usando a funçao round podemos
# arredondar as casas decimais

#cambio = val / dol
#troco = val % dol

cambio_arrendodado = round (val / dol, 2)
troco_arredondado = round(val % dol, 2)

print (f'Com {val} em reais, voce consegue comprar {cambio_arrendodado} dolares \n'
       f'sobrará {troco_arredondado} de troco!')
