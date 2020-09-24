from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        pivot = Counter(A[0])
        for i in range(1, len(A)):
            pivot = pivot & Counter(A[i])
        return list(pivot.elements())


    def commonChars(self, A):
        return list(reduce(Counter.__and__, map(Counter, A)).elements())