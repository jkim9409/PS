# Bubble Sort
#


# n = int(input())

n = 7


def recursive(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return recursive(n // 3) + recursive(n - 1)


print(recursive(n))

# Selection Sort




# Insertion Sort