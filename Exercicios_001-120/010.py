#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

r = float(input('Quantos reias voê tem? '))
dolar = 5.27

if r >= 5.27 and r < 10.54:
    print(f'Com o dolar a US${dolar} você consegue comprar US${r / dolar:.2} dólar!')

elif r <= 0:
    print(f'Com o dolar a US${dolar} voê não consegue comprar nenhum dolár.')

else:
    print(f'Com o dolar a US${dolar} você consegue comprar US${r / dolar:.2} dólares!')
