def get_non_prime_numbers(start, end):
    non_prime_numbers = [num for num in range(start, end + 1) if any(
     num % i == 0 for i in range(2, int(num ** 0.5) + 1))]

    return non_prime_numbers


start_num = 1
end_num = 20
non_prime_nums = get_non_prime_numbers(start_num, end_num)
print(f"Non-prime numbers between {start_num} and {end_num}: {non_prime_nums}")
