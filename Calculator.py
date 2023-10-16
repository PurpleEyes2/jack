import math

print("Какую действие вы хотите сделать: сложение- a+b, вычитание- a-b, умножение - a*b, деление - a : b")
answer = input("Введите действие")
a = int(input("Введите число a"))
b = int(input("Введите число b"))
y = "y"
while y == "y":
    if answer == "сложение":
        sum = a + b
        print(sum)
        print("Хотите попробовать другое действие?")
        break
    elif answer == "вычитание":
        cub = a - b
        print(cub)
        print("Хотите поробовать другое действие?")
        break
    elif answer == "умножение":
        milt = a * b
        print(milt)
        print("Хотите поробовать другое действие?")
        break
    elif answer == "умножение":
        nmn = a / b
        print(nmn)
        print("Хотите поробовать другое действие?")
        break 
      
