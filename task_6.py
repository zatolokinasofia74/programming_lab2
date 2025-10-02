number = int(input("Введіть трицифрове число: "))

digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

max_digit = max(digit1, digit2, digit3)
min_digit = min(digit1, digit2, digit3)

if max_digit == min_digit:
    print(max_digit)
else:
    print(max_digit, min_digit)