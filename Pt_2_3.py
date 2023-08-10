def isarmstrongnumber(number):
    # Переводим число в строку, чтобы узнать кол-во цифр
    numstr = str(number)
    # Получаем кол-во цифр в числе
    numdigits = len(numstr)

    # Сумма чисел, возведенных в степени кол-ва цифр
    armstrongsum = 0
    for digit in numstr:
        armstrongsum += int(digit)**numdigits

    # Проверка, является ли число числом Армстронга
    if number == armstrongsum:
        return True
    else:
        return False


# Тестирование программы
print(isarmstrongnumber(153))  # True
print(isarmstrongnumber(370))  # True
print(isarmstrongnumber(9474))  # True
print(isarmstrongnumber(9475))  # False
