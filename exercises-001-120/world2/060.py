counter = 1
num = int(input("Enter an integer number: "))
current_num = num
total = num
phrase = f"{num}! = {num} "

while counter < num:
        current_num -= 1
        total = total * current_num
        phrase = phrase + f"X {current_num} "
        counter += 1

print(f"\n{phrase} = {total}")
