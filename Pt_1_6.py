def capitalizefirstletter(string):
    words = string.split()

    capitalizedwords = [word.capitalize() for word in words]

    capitalizedstring = ' '.join(capitalizedwords)

    return capitalizedstring


inputstring = input("Введите строку: ")
result = capitalizefirstletter(inputstring)
print(result)
