num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

maxnum = max(num1, num2, num3)
print(f"Наибольшее число: {maxnum}")

if maxnum == num1:
    print(num1, num2, num3)
elif maxnum == num2:
    print(num2, num1, num3)
else:
    print(num3, num2, num1)
