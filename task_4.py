height = float(input("Введіть зріст (м): ")) 
mass = float(input("Введіть масу тіла (кг):"))

index = mass / (height*height)

if index<= 18.5:
    print(f"Your body index is: {index:.2f}, that is underweight")
elif index <=24.9:
    print(f"Your body index is: {index:.2f}, that is normal weight")
else:
    print(f"Your body index is: {index:.2f}, that is overweight")
