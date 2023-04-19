'''
EXERCISE DESCRIPTION:

Write a function that returns the number of prime numbers that exist up to and including a given number.

'''

def count_primes(num):
    prime_count = 0
    for n in range(num+1):
        divisible_nums = []
        if n == 0 or n == 1:
            continue
        for x in range(n+1):
            if x == 0:
                continue
            elif n % x == 0:
                divisible_nums.append(x)
        if divisible_nums == [1,n]:
            prime_count += 1
    return prime_count

# Check
count_primes(100)