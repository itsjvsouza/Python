salario = float(input('Digite seu salário: '))

if salario <= 1250:
    print(f'Seu salário de R${salario} passa a ser de R${salario + (salario * 0.15)}')

else:
    print(f'Seu salário de R${salario} passa a ser de R${salario + (salario * 0.1)}')
