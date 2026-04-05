inicio = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo = inicio
print("\n", inicio, end=" ")

for i in range(9):
    print(termo + razao, end=" ")
    termo = termo + razao
