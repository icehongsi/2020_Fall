from random import randint
def QuickSelect(L, k):
	pivot = L[randint(0, len(L)-1)]
	S, M, B = [], [], [] # S >> values smaller than pivot / M >> values same as pivot / B >> values larger than pivot
	for num in range(len(L)):
		if L[num] < pivot:
			S.append(L[num])
		elif L[num] > pivot:
			B.append(L[num])
		else: #L[num] == pivot:
			M.append(L[num])

	if k <= len(S): # k th small value is in either S or M
		return QuickSelect(S, k)
	elif k > len(S) + len(M): #k th small value is in B
		return QuickSelect(B, k - len(S) - len(M))
	else:
		return pivot

n, k = map(int, input().split(" "))
L = list(map(int, input()[:-1].split(" ")))


print(QuickSelect(L, k))