def find_combinations(nums, target):
    nums.sort()
    combinations = []

    def backtrack(curr_comb, start, curr_sum):
        if curr_sum == target:
            combinations.append(curr_comb[:])
            return
        if curr_sum > target:
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            curr_comb.append(nums[i])
            backtrack(curr_comb, i + 1, curr_sum + nums[i])
            curr_comb.pop()

    backtrack([], 0, 0)
    return combinations


# Example usage
numbers = [2, 4, 6, 3, 7, 5, 1]
target_sum = 10

result = find_combinations(numbers, target_sum)
for combination in result:
    print(combination)
