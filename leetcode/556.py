class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if int("".join(sorted(str(n), reverse=True))) == n:
            return -1 # return when n is the maximum number

        copied = list(str(n)) # transform n into a list
        idx, pivot = 0, 0

        while idx < len(copied) - 1:
            if int(copied[idx]) < int(copied[idx + 1]): #save index of a number when the number is followed by bigger number
                pivot = idx
            idx += 1

        #swap

        temp = copied[pivot]
        copied[pivot] = copied[pivot + 1]
        copied[pivot + 1] = temp

        for i in range(len(copied) - 1, pivot, -1):
            if temp < copied[i] < copied[pivot]:
                temp = copied[i]
                copied[i] = copied[pivot]
                copied[pivot] = temp
                break

        copied = int("".join(copied[:pivot + 1] + sorted(copied[pivot + 1:])))

        if copied > 1 << 31 - 1: # == 2^31 - 1
            return -1
        else:
            return copied



