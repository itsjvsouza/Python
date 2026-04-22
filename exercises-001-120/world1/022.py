name = str(input("Enter your full name: "))
name_split = name.split()

print("Name in uppercase: ", name.upper())
print("\nName in lowercase: ", name.lower())
print("\nNumber of letters in the name: ", len(name) - name.count(" "))
print("\nNumber of letters in the first name: ", len(name_split[0]))
