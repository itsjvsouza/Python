num = int(input("Enter a number from 0 to 9999: "))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f"First digit: {m}")
print(f"\nSecond digit: {c}")
print(f"\nThird digit: {d}")
print(f"\nFourth digit: {u}")
