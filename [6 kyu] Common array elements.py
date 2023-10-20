"""
Given three arrays of integers, return the sum of elements that are common in all three arrays.

For example:

common([1,2,3],[5,3,2],[7,3,2]) = 5 because 2 & 3 are common in all 3 arrays
common([1,2,2,3],[5,3,2,2],[7,3,2,2]) = 7 because 2,2 & 3 are common in the 3 arrays
More examples in the test cases.

Good luck!
 """

# Soltuion

from collections import Counter

def common(a, b, c):
    count_a = Counter(a)
    count_b = Counter(b)
    count_c = Counter(c)

    common_elements = set(count_a.keys()) & set(count_b.keys()) & set(count_c.keys())

    total_sum = sum(min(count_a[element], count_b[element], count_c[element]) * element for element in common_elements)

    return total_sum
