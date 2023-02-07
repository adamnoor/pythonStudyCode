# doesn't work example from the book
# I added a line of code that I think fixes it- should we reach out to the author?


def even_odd(A: [int]) -> [int]:
    next_even, next_odd = 0, len(A) - 1

    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            print(A[next_even], A[next_odd])

    return A


def even_odd_altered(A: [int]) -> [int]:
    next_even, next_odd = 0, len(A) - 1

    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1

        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

    return A
