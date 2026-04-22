reais = float(input("How many reais do you have? "))
dollar = 5.27

if reais >= 5.27 and reais < 10.54:
    print(f"With the dollar at US${dollar} you can buy US${reais / dollar:.2} dollar!")

elif reais <= 0:
    print(f"With the dollar at US${dollar} you cannot buy any dollars.")

else:
    print(f"With the dollar at US${dollar} you can buy US${reais / dollar:.2} dollars!")
