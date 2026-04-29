counter = 0
start = int(input("Enter the first term of the AP: "))
ratio = int(input("Enter the ratio of the AP: "))
term = start
print("\n", start, end=" ")

while counter < 10:
    print(term + ratio, end=" ")
    term = term + ratio
    counter += 1

question = int(input("\n\nHow many terms do you want to see more? (Enter 0 to end) "))

if question > 0:
    
    while question > 0:
        print(term + ratio, end=" ")
        term = term + ratio
        question -= 1
