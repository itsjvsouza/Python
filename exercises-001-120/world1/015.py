days = int(input("How many days did you have the car? "))
km = float(input("How many KM did you drive the car? "))
day_price = days * 60
km_price = km * 0.15
total = day_price + km_price

print(f"You used the car for {days} day(s) and drove {km} kilometers with it.")
print(f"You must pay ${day_price} for the number of days with the car and ${km_price} for the distance driven. \nTotal: ${total}")
