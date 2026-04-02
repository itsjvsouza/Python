#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

a = float(input('Digite ângulo: '))
sen = math.sin(a)
cos = math.cos(a)
tan = math.tan(a)

print(f'O seno, cosseno e tangente do ângulo {a} são respectivamente: {sen:.2}, {cos:.2} e {tan:.2}.')
