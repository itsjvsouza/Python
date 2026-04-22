import math

opp_side = float(input("Enter the length of the opposite side: "))
adj_side = float(input("Enter the length of the adjacent side: "))
hyp = math.hypot(opp_side, adj_side)

print(f"The hypotenuse of the triangle is {hyp}")
