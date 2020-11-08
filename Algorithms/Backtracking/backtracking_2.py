global mark
mark = False

def print_subset(x):
    print([A[i] for i in range(len(x)) if x[i]])

def subset_sum(k,v_sum = 0):
        global mark
        #print(k, v_sum, x)
        if k == len(A):
            if v_sum == S:
                print_subset(x)
                mark = True
        else:
            # code for x[k] = 1 and x[k] = 0
            if v_sum + A[k] > S: # 볼 필요조차 없는 경우
                subset_sum(len(A), v_sum)
            else:
                x[k] = 1
                subset_sum(k+1, v_sum + A[k])
                x[k] = 0
                subset_sum(k+1, v_sum)
                if k == 0 and not mark:
                    print([])
                
# 아래 코드는 수정하지 말고 그대로 사용할 것
A = list(set(int(x) for x in input().split()))
A.sort()
S = int(input()) 
x = [0]*len(A)
subset_sum(0)