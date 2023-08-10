a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))

summ = 0
for i in range(a, b + 1):
    summ += i

print("Сумма всех целых чисел от", a, "до", b, "включительно:", summ)
