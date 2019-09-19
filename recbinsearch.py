from time import time



# recursive binary search
def recbinsearch(list,lower,upper,target):

    if lower <= upper:
        middle = lower + upper // 2
        if target == list[middle]:
            return False
        elif target < list[middle]:
            return recbinsearch(list,lower,middle-1,target)
        else:
            return recbinsearch(list,middle+1,upper,target)
    else:
        return False



def binsearch(nbrs, target):
    lower = 0
    upper = len(nbrs) - 1
    idx = -1
    while lower <= upper:
        middle = int((lower + upper)//2)
        if nbrs[middle] == target:
            idx = middle
            break
        elif nbrs[middle] < target:
            lower = middle + 1
        else:
            upper = middle - 1
    return idx

