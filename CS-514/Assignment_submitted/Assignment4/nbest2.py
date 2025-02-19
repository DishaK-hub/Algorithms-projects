import random

def CartesianProduct( a:list, b:list):
    c = list((i,j) for i in a for j in b)
    return c

def qselect(i:int, a:list)->int:
    if a == []:
        return []
    idx = random.randint(0, len(a) - 1)
    () = a[idx]

    a[0], a[idx] = a[idx], a[0]
    for x,y in a:
        left = [(x,y) for (x,y) in a if (x+y) < pivot]
    len_left = len(left)
    if len_left == i - 1:
        return pivot
    elif len_left < i - 1:
        right = [x for x in a[1:] if x >= pivot]
        return qselect(i - len_left - 1, right)
    else:
        return qselect(i,left)

def nbest(a:list, b:list, k:int):
    result_list=[]
    c = CartesianProduct(a,b)
    for i in range(1,k):
        result_list.append(qselect())


m = [4,1,5,3]
n = [2,6,3,4]

print(nbest(m,n,4))

