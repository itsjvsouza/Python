frase = input('Digite uma frase sem acentos: ').strip().lower()

print(f'\nO nome "{frase}" tem {frase.count('a')} letras "A"')
print(f'\nA primeira letra "A" aparece na posição: {frase.find('a')}')
print(f'\nA última letra "A" aparece na posição: {frase.rfind('a')}')
