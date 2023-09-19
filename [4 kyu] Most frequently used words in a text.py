"""
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
- A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
- Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
- Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
- Matches should be case-insensitive, and the words in the result should be lowercased.
- Ties may be broken arbitrarily.
- If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.

Examples:
top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]
 """

# Soltuion

from collections import Counter
import re

def top_3_words(text):
    text = text.lower()
    cleaned_text = re.sub(r"(?<![a-z])'(?![a-z])|[^a-z']", ' ', text)
    cleaned_text = list(cleaned_text.split(" "))
    counter = Counter(cleaned_text)

    if "" in counter:
        del counter[""]

    top_3 = counter.most_common(3)

    top_3_keys = [key for key,_ in top_3]
    return top_3_keys