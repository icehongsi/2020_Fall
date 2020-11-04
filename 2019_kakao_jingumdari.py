from sys import maxsize


def solution(stones, k):
    answer = max(stones[:k])
    limit = stones[:k].index(answer) + 1  # :k까지의 구간 중 최댓값
    already_checked = k
    while limit + k <= len(stones):
        #print(limit, already_checked)
        max1 = max(stones[already_checked: limit + k])
        if answer >= max1:
            #max2에 대한 비교
            try:
                max2 = max(stones[limit:already_checked])
            except:
                max2 = -maxsize
            if max1 >= max2:
                answer = max1
                temp = limit + k
                limit = stones[already_checked: limit + k].index(max1) + already_checked + 1
                already_checked = temp
            else:
                answer = max2
                temp = limit + k
                limit = stones[limit:already_checked].index(max2) + limit + 1
                already_checked = temp
        else:
            temp = limit + k
            limit = stones[already_checked: limit + k].index(max1) + already_checked + 1
            already_checked = temp
    return answer


result = solution(
    [2, 4, 5, 3, 2, 1, 4, 2, 5, 1],	3
)

print(result)