soma = 0

for i in range(0, 6):
    num = int(input("Digite o número: "))
    
    if num % 2 == 0:
        soma += num

print(f"\nA soma dos pares é: {soma}")
