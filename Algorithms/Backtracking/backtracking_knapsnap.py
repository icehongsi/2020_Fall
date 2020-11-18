def fractionalKnapsnack (idx, size):
    result = 0
    while idx < n:
        if size < items[idx][0]:
            result += items[idx][2] * size
            break
        else: #size >= idx:
            result += items[idx][1]
            size = size - items[idx][0]
            idx += 1

    return result

def knapsnack(idx, size): #idx: index of items, size: remnant size
    global MP
    if idx >= n or size <= 0:
        return #floor condition of recursive function
    #print(included)
    #print(items[idx], size, idx)
    total_point = sum(included[i] * items[i][1] for i in range(idx))
    total_size = sum(included[i] * items[i][0] for i in range(idx))
    if items[idx][0] <= size: #case of including (idx)th item into the bag
        B = fractionalKnapsnack(idx+1, size-items[idx][0]) #expected value when (idx)th item is included
        #print("B", B)
        if MP < total_point + items[idx][1] + B:
            included[idx] = 1 #mark as 'included'
            #print("included: ", idx, included)
            MP = max(MP, total_point + items[idx][1])
            knapsnack(idx+1, size - items[idx][0])
    included[idx] = 0 #mark as 'excluded'
    #print("excluded: ", idx, included)
    B = fractionalKnapsnack(idx+1, size)
    if MP < total_point + B:
        included[idx] = 0
        knapsnack(idx+1, size)

K = int(input()) #size of bag
n = int(input()) #n of an item
size = list(map(int, input().split()))
value = list(map(int, input().split()))
items = [
    [size[i], value[i], value[i] / size[i]] #item[0][0]: size, item[0][1]: value, item[0][2]: efficacy
     for i in range(n)]
items = sorted(items, key = lambda x: x[2], reverse = True)
included, MP = [0] * n, -1<<63
knapsnack(0, K)
print(MP)