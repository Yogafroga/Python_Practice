def create_letter_count_dict(input_string):
    letter_count_dict = {}
    for char in input_string:
        if char.isalpha():
            if char in letter_count_dict:
                letter_count_dict[char] += 1
            else:
                letter_count_dict[char] = 1
    return letter_count_dict


string = input("Enter a string: ")
letter_c_dict = create_letter_count_dict(string)
print(letter_c_dict)
