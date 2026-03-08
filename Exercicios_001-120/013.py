#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salário = float(input('Qual o seu salário? '))
aumento = salário + salário * 0.15

print(f'O seu salário de R${salário} recebeu um aumento de 15% e agora passa a ser de R${aumento}')
