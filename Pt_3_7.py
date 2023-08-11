def createvoweldict(string):
    vowels = 'a', 'e', 'i', 'o', 'u'
    voweldict = {}
    for letter in string:
        if letter.lower() in vowels:
            voweldict[letter] = True
        else:
            voweldict[letter] = False
    return voweldict


inputstring = input("Enter a string: ")
resultdict = createvoweldict(inputstring)
print(resultdict)
