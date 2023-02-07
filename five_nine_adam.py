# I did 5.9 (linear space, quadratic time).  Going to check the space and time complexities.
# Used some high level hints (to leverage the index) to solve it.
# Also I needed to look up a bunch of syntactical stuff.


def all_primes(number: int) -> [int]:
    prime_bool = [True for _ in range(number + 1)]
    prime_bool[0] = False
    prime_bool[1] = False
    prime_numbers = []

    def is_prime(i) -> bool:
        high = int(i/2)+1
        low = 2
        for e in range(low, high):
            if i % e == 0:
                return False
        return True

    if number < 2:
        return []
    elif number == 2:
        return [2]
    elif number == 3:
        return [2, 3]
    else:
        for n in range(4, number + 1):
            prime_bool[n] = is_prime(n)

        for index, element in enumerate(prime_bool):
            if element and index > 1:
                prime_numbers.append(index)

        return prime_numbers
