dias = int(input('Quantos dias você passou com o carro? '))
km = float(input('Quantos KM você andou com o carro? '))
preço_dia = dias * 60
preço_km = km * 0.15
total = preço_dia + preço_km

print(f'Você usou o carro por {dias} dia(s) e andou {km} kilometros com ele.')
print(f'Você deve pagar R${preço_dia} pela quantidade de dias com o carro e R${preço_km} pela distância rodada. \nTotal: R${total}')
