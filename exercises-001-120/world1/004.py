something = input("Enter something: ")

print("The primitive type of this value is: ", type(something))
print("Does it only have spaces? ", something.isspace())
print("Is it a number? ", something.isnumeric())
print("Is it alphabetical? ", something.isalpha())
print("Is it in uppercase? ", something.isupper())
print("Is it in lowercase? ", something.islower())
print("Is it capitalized? ", something.istitle())
