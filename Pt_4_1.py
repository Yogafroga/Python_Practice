def findlargestnumber(num):
    # Convert number to string
    numstr = str(num)

    # Sort the digits in descending order
    sortedstr = ''.join(sorted(numstr, reverse=True))

    # Convert string back to integer
    largestnum = int(sortedstr)

    return largestnum


# Test the function
number = 111294985
largestnumber = findlargestnumber(number)
print(f"The largest number that can be formed is: {largestnumber}")
