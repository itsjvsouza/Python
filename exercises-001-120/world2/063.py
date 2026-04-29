qnt_num = int(input("Enter the quantity of numbers: "))
counter = 3
term0 = 0
term1 = 1
print(term0, term1, end=" ")

while counter <= qnt_num:
    term = term0 + term1
    term0 = term1
    term1 = term
    counter += 1
    print(term, end=" ")
