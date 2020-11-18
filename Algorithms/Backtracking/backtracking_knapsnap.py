def fractionalKnapsnack (idx, size):
    result = 0
    while True:
        if idx >= n:
            break
        elif items[idx][0] > size: #when the item cannot be loaded as a whole
            result += items[idx][2] * size
            break
        else: #when index meets an end or size is large enough
            result += items[idx][1]
            size -= items[idx][0]
            idx += 1
    return result

def knapsnack(idx, size): #idx: index of items, size: remnant size
    if idx >= n or size <= 0:
        return #floor condition of recursive function
    points = sum(included[i] * items[i][0] for i in idx)
    size = sum(included[i] * items[i][1] for i in idx)
    

    




K = int(input()) #size of bag
n = int(input()) #n of an item
size = list(map(int, input().split()))
value = list(map(int, input().split()))
items = [
    [size[i], value[i], value[i] / size[i]] #item[0][0]: size, item[0][1]: value, item[0][2]: efficacy
     for i in range(n)]
items = sorted(items, key = lambda x: x[2], reverse = True)
included = [0] * n

print(items)
print(included)