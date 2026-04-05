valor = float(input("Digite o valor do produto: "))
forma = int(input("""
1 - A vista dinheiro/cheque
2 - A vista no cartão
3 - 2x no cartão
4 - 3x ou mais no cartão
Qual a forma de pagamento? """))

if forma == 1:
    print(f"Valor a pagar: {valor - (valor * 0.1)}")

elif forma == 2:
    print(f"Valor a pagar: {valor - (valor * 0.05)}")

elif forma == 3:
    print(f"Valor a pagar: {valor}")

elif forma == 4:
    print(f"Valor a pagar: {valor + (valor * 0.2)}")

else:
    print("Opção inválida.")
