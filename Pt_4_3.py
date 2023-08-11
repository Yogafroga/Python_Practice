def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(beginning, final):
    primes = []
    for num in range(beginning, final + 1):
        if is_prime(num):
            primes.append(num)
    return primes


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Prime numbers in the range", start, "to", end, "are:")
print(find_primes(start, end))
