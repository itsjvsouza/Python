num = 0
sum = 0
counter = 0
question = ""

while question != "n":
    num = int(input("\nEnter an integer number: "))
    sum += num
    counter += 1

    if counter == 1:
        highest = num
        lowest = num
    else:
        if num > highest:
            highest = num
        
        if num - lowest < 0:
            lowest = num
    question = input("Do you want add another number? (Y/N) ").lower()

print(f"""
The avarage of the {counter} numbers given is: {sum / counter:.2f}
The highest number given is: {highest}
The lowest number given is: {lowest}""")
