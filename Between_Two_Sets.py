

# Problem Statement
# You are given two arrays of integers A and B.
# Find how many integers x satisfy the following conditions:
# Every element in array A is a factor of x.
# x is a factor of every element in array B.
# Return the count of such integers.

# A = [2, 4]
# B = [16, 32, 96]

# Output: 3
# Valid numbers: 4, 8, 16


def getTotalX(a, b):
    start = max(a)
    end = min(b)
    count = 0

    for x in range(start, end + 1):
        valid = True

        # Check condition 1: all elements in a divide x
        for num in a:
            if x % num != 0:
                valid = False
                break

        # Check condition 2: x divides all elements in b
        if valid:
            for num in b:
                if num % x != 0:
                    valid = False
                    break

        if valid:
            count += 1

    return count
