start = int(input("Enter the first term of the AP: "))
ratio = int(input("Enter the ratio of the AP: "))
term = start
print("\n", start, end=" ")

for i in range(9):
    print(term + ratio, end=" ")
    term = term + ratio
