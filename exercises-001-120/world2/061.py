counter = 0
start = int(input("Enter the first term of the AP: "))
ratio = int(input("Enter the ratio of the AP: "))
term = start
print("\n", start, end=" ")

while counter < 10:
    print(term + ratio, end=" ")
    term = term + ratio
    counter += 1
