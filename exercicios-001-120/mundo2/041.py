ano = int(input("Em que ano você nasceu? "))
idade = 2026 - ano

if idade >= 0 and idade <= 9:
    print("MIRIM")

elif idade > 9 and idade <=14:
    print("INFANTIL")

elif idade > 14 and idade <=19:
    print("JÚNIOR")

elif idade > 19 and idade <=25:
    print("SÊNIOR")

elif idade > 25:
    print("MASTER")

else:
    print("DATA INVÁLIDA")
