#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias você passou com o carro? '))
km = float(input('Quantos KM você andou com o carro? '))
preço_dia = dias * 60
preço_km = km * 0.15
total = preço_dia + preço_km

print(f'Você usou o carro por {dias} dia(s) e andou {km} kilometros com ele.')
print(f'Você deve pagar R${preço_dia} pela quantidade de dias com o carro e R${preço_km} pela distância rodada. \nTotal: R${total}')
