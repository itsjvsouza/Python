word = input("Enter a word: ").strip().lower()
word2 = ""

for i in range(len(word) - 1, -1, -1):
    word2 += word[i]

if word == word2:
    print(f"\nThe word {word} is a palindrome.")
else:
    print(f"\nThe word {word} is not a palindrome.")
