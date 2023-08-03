points = int(input("Введите количество очков: "))

if points == 3:
    print("Выигрыш")
elif points == 1:
    print("Ничья")
elif points == 0:
    print("Проигрыш")
else:
    print("Некорректное количество очков")
