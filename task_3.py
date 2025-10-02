number=int (input("ВВедіть число: "))

first_number = number // 10
second_number = number - first_number*10

if first_number > second_number:
    print("1")
elif second_number > first_number:
    print("2")
else:
    print("=")


