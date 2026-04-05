v = int(input('Qual a velocidade do carro? '))

if v > 80:
    print('\nVocê foi multado!')
    print(f'\nVocê pagará R${(v - 80) * 7} de multa.')

else:
    print('Você está dentro do limite de velocidade!')
