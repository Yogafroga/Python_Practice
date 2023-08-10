def findmaxdigitposition(number):
    # convert the number to a string
    numberstr = str(number)
    
    # get the maximum digit
    maxdigit = max(numberstr)
    
    # find the reverse position of the maximum digit
    reverseposition = numberstr[::-1].index(maxdigit)
    
    # find the forward position of the maximum digit
    forwardposition = numberstr.index(maxdigit)

    # return both positions
    return len(numberstr) - reverseposition, forwardposition + 1


# test the function
num = int(input("Enter a natural number: "))
result = findmaxdigitposition(num)
print("Reverse position of maximum digit:", result[0])
print("Forward position of maximum digit:", result[1])
