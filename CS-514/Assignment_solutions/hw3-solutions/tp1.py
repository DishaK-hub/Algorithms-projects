#qselect
import random

def qselect(i:int, a:list):
    if (a==[]):
        return []
    idx = random.randint(0,len(a)-1)
    pivot = a[idx]
    a[0],a[idx] = a[idx],a[0]

    left = [x for x in a if x < pivot]
    len_left = len(left)
    if ( len_left == i - 1):
        return pivot
    elif(len_left < i-1 ):
        right =[x for x in a if x> pivot]
        return qselect(i - len_left -1, right)
    else:
        return qselect(i,left)

print(qselect( 4, [1,2,7,1212,32,23,143,232]))
