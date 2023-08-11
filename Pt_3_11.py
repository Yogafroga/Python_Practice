def count_unique_letters(string):
    # Convert the input string to lowercase
    string = string.lower()

    # Create a dictionary using dict comprehensions
    unique_letters = {letter: string.count(letter) for letter in string if letter.isalpha()}

    return unique_letters


# Test the function
input_string = input("Enter a string: ")
result = count_unique_letters(input_string)
print(result)
