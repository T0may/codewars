"""
A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.

Write a function that computes the nth smallest Hamming number.

Specifically:

The first smallest Hamming number is 1 = 203050
The second smallest Hamming number is 2 = 213050
The third smallest Hamming number is 3 = 203150
The fourth smallest Hamming number is 4 = 223050
The fifth smallest Hamming number is 5 = 203051
The 20 smallest Hamming numbers are given in the Example test fixture.

Your code should be able to compute the first 5 000 ( LC: 400, Clojure: 2 000, Haskell: 12 691, NASM, C, D, C++, Go and Rust: 13 282 ) Hamming numbers without timing out.
"""

def hamming(n):
    hamming_list = [1]
    i,j,k = 0, 0, 0
    next_hamming = 0

    while len(hamming_list) < n:
        next_hamming_2 = hamming_list[i] * 2
        next_hamming_3 = hamming_list[j] * 3
        next_hamming_5 = hamming_list[k] * 5
        candidates = [next_hamming_2, next_hamming_3, next_hamming_5]

        next_hamming = min(candidates)

        hamming_list.append(next_hamming)

        if next_hamming == candidates[0]:
            i += 1
        if next_hamming == candidates[1]:
            j += 1
        if next_hamming == candidates[2]:
            k += 1

    return next_hamming if n != 1 else 1