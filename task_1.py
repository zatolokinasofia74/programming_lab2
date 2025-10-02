circle = float(input("Введіть радіус кола: "))
square = float(input("Введіть сторону квадрата: "))

radius_circle = 3.14 * circle**2  
square_radius = square**2

if radius_circle > square_radius:
    print("Площа кола більша")
elif square_radius > radius_circle:
    print("Площа квадрата більша")
else:
    print("Площі рівні")