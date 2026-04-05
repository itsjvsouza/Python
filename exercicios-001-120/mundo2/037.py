num = int(input("Digite um número inteiro: "))
base = int(input("""
1 - Binário
2 - Octal
3 - Hexadecimal
                 
Escolha a base de conversão: """))

if base == 1:
    print(f"\n{num} convertido para binário é: {bin(num)}")

elif base == 2:
    print(f"\n{num} convertido para octal é: {oct(num)}")

elif base == 3:
    print(f"\n{num} convertido para hexadecimal é: {hex(num)}")

else:
    print("\nOpção inválida.")
