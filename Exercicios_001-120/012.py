#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o preço do produto: '))
novo_preço = preço - preço * 0.05

print(f'O seu produto com o desconto de 5% sai de R${preço} para R${novo_preço}')
