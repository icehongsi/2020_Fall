from collections import Counter
def groupAnagrams(strs):
    anag_dict = {}
    for i in strs:
        temp = "".join(sorted(i))
        try:
            anag_dict[temp].append(i)
        except:
            anag_dict[temp] = [i]
    return list(anag_dict.values())

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])