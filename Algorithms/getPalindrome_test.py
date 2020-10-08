def palindrome(s, left, right):
    if right - left < 1:
        return True
    return s[left] == s[right] and palindrome(s, left+1, right-1)


s = "helloolleh"#input().lower()
s = "".join(s.split())
result = palindrome(s, 0, len(s)-1)
print(result)