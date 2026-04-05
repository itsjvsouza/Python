ano = int(input("Em que ano você nasceu? "))
idade = 2026 - ano

if idade == 18:
    print("\nVocê deve se alistar esse ano.")

elif idade < 18:
    
    if 18 - idade == 1:
        print("\nFalta 1 ano para você se alistar.")
    
    else:
        print(f"\nFaltam {18 - idade} anos para você se alistar.")

else:

    if idade - 18 == 1:
        print("\nVocê está 1 ano atrasado!")
    
    else:
        print(f"\nVocê está {idade - 18} anos atrasado!")
