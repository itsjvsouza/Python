nota1 = float(input("Digite a priemira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print("\n\033[1;31mREPROVADO\033[m\n")

elif media >= 5 and media < 7:
    print("\n\033[1;33mRECUPERAÇÃO\033[m\n")

else:
    print("\n\033[1;32mAPROVADO\033[m\n")
