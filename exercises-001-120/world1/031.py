dist = float(input("Enter the travel distance in km: "))

if dist <= 200:
    print(f"For a trip of {dist}km you will pay ${dist * 0.5}.")

else:
    print(f"For a trip of {dist}km you will pay ${dist * 0.45}.")
