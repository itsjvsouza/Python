r1 = float(input('Digite o valor da primeira reta do triângulo: '))
r2 = float(input('\nDigite o valor da segunda reta do triângulo: '))
r3 = float(input('\nDigite o valor da terceira reta do triângulo: '))

if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print('Não é possível formar um triângulo com essas retas.')

elif r1 != r2 and r1 != r3 and r2 != r3:
    print("O triângulo formado é escaleno.")

elif r1 == r2 and r2 == r3:
    print("O triângulo formado é equilátero.")

else:
    print("O triângulo formado é isóceles.")
