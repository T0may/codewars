""" Welcome
This kata is inspired by This Kata (https://www.codewars.com/kata/odd-even-string-sort)

We have a string s

We have a number n

Here is a function that takes your string, concatenates the even-indexed chars to the front, odd-indexed chars to the back.

Examples
s = "Wow Example!"
result = "WwEapeo xml!"
s = "I'm JomoPipi"
result = "ImJm ii' ooPp"
The Task:
return the result of the string after applying the function to it n times.

example where s = "qwertyuio" and n = 2:

after 1 iteration  s = "qetuowryi"
after 2 iterations s = "qtorieuwy"
return "qtorieuwy"
Note
there's a lot of tests, big strings, and n is greater than a billion

so be ready to optimize.

after doing this: do it's best friend! """

# Soltuion

def jumbled_string(s, n):

    comparison = s
    count = 1
    s = s[::2] + s[1::2]

    while True:
        s = s[::2] + s[1::2]
        count += 1
        if s == comparison:
            for _ in range(n%count):
                s = s[::2] + s[1::2]
            break

    return s
