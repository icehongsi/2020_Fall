import time
def arrayNesting(nums):
    result = 0
    check = [False]*len(nums)
    for i in range(len(nums)):
        pivot = 0
        if check[i] == False: # unvisited element
            check[i] = True
            pivot += 1
            nested = nums[i]
            while check[nested] == False:
                check[nested] = True
                nested = nums[nested]
                pivot += 1
                if nums[nested] == i:
                    pivot += 1
                    break
            if pivot > result:
                result = pivot
    return result



arrayNesting([5,4,0,3,1,6,2])



def arrayNesting(nums):
    result = 0
    check = [False]*len(nums)
    for i in range(len(nums)):
        pivot = 0
        if check[i] == False: # unvisited element
            nest = i
            while True:
                check[nest] = True
                pivot += 1
                if check[nums[nest]]:
                    break
                else:
                    nest = nums[nest]
            if pivot > result: result = pivot
    return result

print(arrayNesting([5,4,0,3,1,6,2]))