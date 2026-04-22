import math

angle = float(input("Enter the angle: "))
# Note: math functions in Python expect radians
sin = math.sin(angle)
cos = math.cos(angle)
tan = math.tan(angle)

print(f"The sine, cosine, and tangent of the angle {angle} are respectively: {sin:.2}, {cos:.2}, and {tan:.2}.")
