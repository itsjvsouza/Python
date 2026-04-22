phrase = input("Enter a phrase without accents: ").strip().lower()

print(f"\nThe phrase {phrase} has {phrase.count("a")} letters A")
print(f"\nThe first letter A appears at position: {phrase.find("a")}")
print(f"\nThe last letter A appears at position: {phrase.rfind("a")}")
