valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Em quantos anos pretende pagar? "))

prestacao = valor / (anos * 12)

if prestacao > salario * 0.3:
    print("Seu empréstimo foi negado!")

else:
    print("Seu empréstimo foi aprovado!")
