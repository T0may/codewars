"""
You are given a string s. Every letter in s appears once.

Consider all strings formed by rearranging the letters in s. After ordering these strings in dictionary order, return the middle term. (If the sequence has a even length n, define its middle term to be the (n/2)th term.)

Example
For s = "abc", the result should be "bac".

 The permutations in order are: "abc", "acb", "bac", "bca", "cab", "cba" So, The middle term is "bac".

Input/Output
[input] string s
unique letters (2 <= length <= 26)

[output] a string
middle permutation.
 """

# Soltuion
# This solution is correct, but timed out on codewars when testing larger strings

def get_perms(s):
    if len(s) == 1:
        return [s]

    all_perms = []
    for i in range(len(s)):
        first_char = s[i]
        rest = s[:i] + s[i+1:]
        for perm in get_perms(rest):
            all_perms.append(first_char + perm)
    return all_perms

def middle_permutation(s):
    perms = get_perms(s)
    perms.sort()

    index = len(perms) // 2
    return perms[index - 1]