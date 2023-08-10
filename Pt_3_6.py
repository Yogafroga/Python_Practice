def create_binary_dictionary():
    binary_dict = {}
    for i in range(1, 11):
        binary_dict[i] = bin(i)[2:]
    return binary_dict


binary_dictionary = create_binary_dictionary()
print(binary_dictionary)
