dist = float(input('Digite a distância da viagem em km: '))

if dist <= 200:
    print(f'Para uma viagem de {dist}km você pagará R${dist * 0.5}.')

else:
    print(f'Para uma viagem de {dist}km você pagará R${dist * 0.45}.')
