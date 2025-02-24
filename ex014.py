#Exercício Python 14: Escreva um programa que converta uma temperatura
#digitando em graus Celsius e converta para graus Fahrenheit.

# tomando ciencia de que a formula de Celcius para fahrenheit é
# igual a ( °C × 9/5) + 32 = °F

c = float (input ('Digite a temperatura em graus Celcius: '))
f = ( c * 9/5) + 32

print (f'A temperatura {c}°C equivalem a {f}°F.')

