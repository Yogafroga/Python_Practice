def squarenumbers(numbers):
    return [num for num in numbers if int(num ** 0.5) ** 2 == num]


# Example usage
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squarenumbers = squarenumbers(nums)
print(squarenumbers)
