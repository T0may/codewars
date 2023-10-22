"""
There are no explanations. You have to create the code that gives the following results in Python, Ruby, and Haskell:

one_two_three(0) == [0, 0]
one_two_three(1) == [1, 1]
one_two_three(2) == [2, 11]
one_two_three(3) == [3, 111]
one_two_three(19) == [991, 1111111111111111111]
"""

# Soltuion

def one_two_three(n):

    if n == 0:
        return[0, 0]

    second_el = '1' * n
    first_el = ""

    while n > 0:
        if n >= 9:
            first_el += "9"
        else:
            first_el += str(n)
            n = 0
        n -= 9

    return [int(first_el), int(second_el)]