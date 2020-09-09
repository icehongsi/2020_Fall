import re

def isPalindrome(s):

    s = re.sub("[^0-9a-z]", "", s.lower())
    return s == s[::-1]

isPalindrome("Hello, World!")