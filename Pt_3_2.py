def fibonacci(n):
    fiblist = [0, 1]  # список, содержащий первые два числа Фибоначчи
    while fiblist[-1] < n:
        fiblist.append(fiblist[-1] + fiblist[-2])
    return fiblist


example = fibonacci(100)
print(example)

# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
