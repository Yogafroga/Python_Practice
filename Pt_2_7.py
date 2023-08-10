def sum_negative_numbers():
    summ = 0
    while True:
        number = int(input("Enter a number: "))
        if number >= 0:
            break
        summ += number
    return summ


result = sum_negative_numbers()
print("Sum of negative numbers:", result)
