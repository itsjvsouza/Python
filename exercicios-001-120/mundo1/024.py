cidade = input('Digite o nome da cidade: ').strip()

print(f'A cidade "{cidade}" começa com Santo? {'SANTO' in cidade[:5].upper()}')
