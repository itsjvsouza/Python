import math

cat_o = float(input('Digite o comprimento do cateto oposto: '))
cat_a = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(cat_o, cat_a)

print(f'A hipotenusa é do triângulo é {hip}')
