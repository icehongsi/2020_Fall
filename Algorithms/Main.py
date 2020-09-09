import random
import time

def prefixSum1(X,n): #O(n^2)
  S = []
  for i in range(n):
    S.append(0)
    for j in range(i):
      S[i] += X[j]

def prefixSum2(X,n):
    S = [X[0]]
    for i in range(1,n):
        S.append(S[i-1]+X[i])

random.seed()
# random 함수 초기화
# n 입력받음
# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
X = [random.randint(-999,999) for i in range(int(input()))]
# prefixSum1 호출
before = time.perf_counter()
prefixSum1(X,len(X))
print(time.perf_counter() - before)
# prefixSum2 호출
before = time.perf_counter()
prefixSum2(X, len(X))
print(time.perf_counter() - before)
