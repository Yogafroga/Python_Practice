def permutations(lst):
    # Base case: If the list is empty, return an empty list
    if len(lst) == 0:
        return []

    # Base case: If the list contains only one element, return a list containing that element
    if len(lst) == 1:
        return [lst]

    # Recursive case: Find permutations for all elements except the first one
    all_permutations = []
    for i in range(len(lst)):
        current_element = lst[i]
        remaining_elements = lst[:i] + lst[i + 1:]
        for p in permutations(remaining_elements):
            all_permutations.append([current_element] + p)

    return all_permutations


# Test the function
my_list = [1, 2, 3, 4, 5]
print(permutations(my_list))
