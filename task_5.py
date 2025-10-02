t = int(input("Введіть час у хвилинах: "))

position = t % 5

if position < 3:
    print("green")
else:
    print("red")