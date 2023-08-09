def capitalizefirstletter(string):
    # Разбиваем строку на слова
    words = string.split()

    # Применяем функцию str.capitalize к каждому слову
    capitalizedwords = [word.capitalize() for word in words]

    # Соединяем слова обратно в строку
    capitalizedstring = ' '.join(capitalizedwords)

    return capitalizedstring


# Пример использования
inputstring = input("Введите строку: ")
result = capitalizefirstletter(inputstring)
print(result)
