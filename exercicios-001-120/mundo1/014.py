#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Qual a temperatura em graus celsius? '))
fahrenheit = (celsius * 9/5) + 32

print(f'A temperatura de {celsius}°C é igual a {fahrenheit}°F')
