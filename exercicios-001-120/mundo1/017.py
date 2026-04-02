#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

cat_o = float(input('Digite o comprimento do cateto oposto: '))
cat_a = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(cat_o, cat_a)

print(f'A hipotenusa é do triângulo é {hip}')
