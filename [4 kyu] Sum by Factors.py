""" Given an array of positive or negative integers

 I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:
I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result. """

# Soltuion

def sum_for_list(lst):
    prime_factors_sum = {}
    for num in lst:
        n = abs(num)
        i = 2
        while i * i <= n:
            if n % i == 0:
                while n % i == 0:
                    n //= i
                prime_factors_sum[i] = prime_factors_sum.get(i, 0) + num
            i += 1
        if n > 1:
            prime_factors_sum[n] = prime_factors_sum.get(n, 0) + num

    result = [[factor, prime_factors_sum[factor]] for factor in sorted(prime_factors_sum.keys())]
    return result

