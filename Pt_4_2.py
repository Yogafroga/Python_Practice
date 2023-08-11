def find_palindromes(string):
    palindromes = []
    n = len(string)

    # Iterate over all possible substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = string[i:j]

            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                palindromes.append(substring)

    return palindromes


# Example usage
examp_string = input("Enter a string: ")
palindrome_list = find_palindromes(examp_string)
print("Palindromes:", palindrome_list)
