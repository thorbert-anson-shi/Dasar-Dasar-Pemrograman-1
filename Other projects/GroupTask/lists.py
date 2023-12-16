import time
import math


def generate_primes(min, max):
    bitset = [True for num in range(max + 1)]
    bitset[0] = bitset[1] = False

    prime_sum = 0

    for i in range(2, max + 1):
        if bitset[i]:
            if min <= i <= max:
                prime_sum += i
            else:
                bitset[i] = False
            for j in range(2 * i, max + 1, i):
                bitset[j] = False
    return [i for i in range(len(bitset)) if bitset[i]], prime_sum


def generate_primes2(min, max):
    results = []
    for number in range(min, max + 1):
        is_prime = True
        for i in range(2, math.floor(math.sqrt(number)) + 1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime and number > 1:
            results.append(number)

    return sum(results)


def generate_primes3(min, max):
    results = []
    multiples = []
    for number in range(3, max + 1, 2):
        if number in multiples:
            pass
        else:
            results.append(number)
            for i in range(number * 2, max + 1, number):
                multiples.append(number)

    print(results)
    return sum(results)


generate_primes3(10, 100)

# st1 = time.time()
# generate_primes(10, 10000)
# en1 = time.time()

# print(f"{en1-st1:.5}")

# st2 = time.time()
# generate_primes2(10, 10000)
# en2 = time.time()


# print(f"{en2-st2:.5}")
