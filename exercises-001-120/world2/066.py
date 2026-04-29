sum = 0
counter = 0

while True:
    num = int(input("Enter an interger number (press 999 to stop): "))
     
    if num != 999:
        sum += num
        counter += 1
    else:
        break

print(f"{counter} numbers were entered and the sum between them is {sum}")
