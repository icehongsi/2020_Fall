import time
from collections import deque
#class Solution:
def lengthOfLongestSubstring(s):
    if len(s) == 0: return 0
    alphabet = deque()
    start, end, substring = 0, 0, 0
    while start < len(s):
        print("while")
        temp = 0
        while end < len(s) and s[end] not in alphabet:
            alphabet.append(s[end])
            end += 1
            print(alphabet)
            temp += 1
            print(start, end)
        if len(alphabet) > substring:
            substring = len(alphabet)
        if end == len(s):
            return substring
        while end < len(s):
            temp_string = alphabet.popleft()
            print(temp_string)
            start += 1
            if temp_string == s[end]: break



lengthOfLongestSubstring("abcabcbb")


#fastest solution
def lengthOfLongestSubstring(s):
    if len(s) == 0: return 0
    alphabet = {}
    max_length = start = 0
    for i, v in enumerate(s):
        if v in alphabet and start <= alphabet[v]: # when the alphabet is already used and 'start' variable is equal or smaller than alphabet[v]
            start = alphabet[v] + 1 #alphabet[v] + 1 will be a new start
        else:
            if max_length < i-start+1:
                max_length = i-start+1 #adjust maximum length
        alphabet[v] = i #assign new index
    return max_length




print(lengthOfLongestSubstring("abcabcbb"))