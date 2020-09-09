from collections import Counter
import re

def mostCommonWord(paragraph, banned):
    paragraph = re.sub(r"[^\w | \s ]", " ", paragraph.lower())
    while paragraph.count("  ") > 0:
        paragraph = paragraph.replace("  ", " ")
    paragraph = Counter(tuple(paragraph.split(" ")))
    index = 0
    while paragraph.most_common(index+1)[index][0] in banned:
        index += 1
    return paragraph.most_common(index+1)[index][0]

print(mostCommonWord(paragraph = "a, a, a, a, b,b,b,c, c", banned = ["a"]))