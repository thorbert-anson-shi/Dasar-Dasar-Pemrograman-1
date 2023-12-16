import math


def prime(min: int, max: int):
    results = []
    for number in range(min, max + 1):
        is_prime = True
        for i in range(2, math.floor(math.sqrt(number)) + 1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime and number > 1:
            results.append(number)

    print(results)
    return sum(results)


print(prime(0, 100000))
