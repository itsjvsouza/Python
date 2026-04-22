weight = float(input("What is your weight? "))
height = float(input("What is your height? "))
bmi = weight / height ** 2

if bmi <= 18.5:
    print("Underweight")

elif bmi > 18.5 and bmi <= 25:
    print("Ideal weight")

elif bmi > 25 and bmi <= 30:
    print("Overweight")

elif bmi > 30 and bmi <= 40:
    print("Obesity")

else:
    print("Morbid obesity")
