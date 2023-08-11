def rot13(string):
    result = ""
    for char in string:
        if char.isalpha():
            ascii_num = ord(char)
            if char.islower():
                result += chr((ascii_num - 97 + 13) % 26 + 97)
            else:
                result += chr((ascii_num - 65 + 13) % 26 + 65)
        else:
            result += char
    return result


text = input("Enter a string to encode: ")
encoded_text = rot13(text)
print("Encoded text: ", encoded_text)
