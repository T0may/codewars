""" How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

Test examples:

"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!" """

# Soltuion

def rot13(message):

    alphabet = 	["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    deciphered_string = ""

    for letter in message:

        if letter.isalpha():
            if letter.isupper():
                alphabet = [el.upper() for el in alphabet]
            else:
                alphabet = [el.lower() for el in alphabet]
            index = alphabet.index(letter)
            deciphered_string += alphabet[(index + 13) % 26]
        else:
            deciphered_string += letter

    return deciphered_string