from collections import Counter
import time
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):  # no need to take into consideration
            return False
        elif len(s1) == 0:
            return True

        subset, string = Counter(s1), list(s2)
        idx = 0
        while idx <= len(string) - len(subset):
            if string[idx] in subset:
                check = subset
                for i in range(idx, idx + len(subset)):
                    if string[i] in check:
                        if check[string[i]] == 0:
                            idx = i
                            break
                        else:
                            check[string[i]] -= 1
                    else:
                        idx = i
                        break
            idx += 1

        return False


'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):  # no need to take into consideration
            return False
        elif len(s1) == 0:
            return True

        subset, string = sorted(list(s1)), list(s2)
        idx = 0
        while idx <= len(string) - len(subset):
            if string[idx] in subset:
                if sorted(string[idx: idx + len(subset)]) == subset:
                    return True
            idx += 1

        return False

Runtime: 3868 ms, faster than 11.15% of Python3 online submissions for Permutation in String.
Memory Usage: 13.8 MB, less than 64.45% of Python3 online submissions for Permutation in String.
비효율적 알고리즘
'''


from collections import Counter

def checkInclusion(s1, s2):
    if len(s1) > len(s2):  # no need to take into consideration
        return False
    elif len(s1) == 0:
        return True
    string = list(s2)
    idx = 0
    while idx <= len(string) - len(s1):
        if string[idx] in s1:
            check = Counter(s1)
            for i in range(idx, idx + len(s1)):
                if string[i] in check:
                    if check[string[i]] == 0:
                        idx += string[idx:].index(string[i])
                        break
                    else: check[string[i]] -= 1
                else:
                    idx = i
                    break
            if sum(check.values()) == 0:
                return True
        idx += 1
    return False


print(checkInclusion("hello","ooolleoooleh"))
#print(checkInclusion("adc", "dcda"))


def checkInclusion(s1, s2):
    l1 = [0] * 26
    l2 = [0] * 26
    for x in s1:
        l1[ord(x) - ord('a')] += 1 #알파벳별로 몇 개씩 있는지 담고 있는 리스트
    print(l1)
    for i in range(len(s2)): # 순열 존재 여부를 찾을 리스트
        l2[ord(s2[i]) - ord('a')] += 1
        if i >= len(s1):
            l2[ord(s2[i - len(s1)]) - ord('a')] -= 1
        if l1 == l2:
            return True
    return False

print(checkInclusion("hello","ooolleoooleh"))