'''
EXERCISE DESCRIPTION:

Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

'''


import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    letters_in_str = set(str1.replace(" ", "").lower())
    alphabet = set(alphabet)
    return alphabet == letters_in_str

#Check
ispangram("The quick brown fox jumps over the lazy dog")