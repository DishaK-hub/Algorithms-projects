from heapq import heapify, heappop, heappush
from collections import defaultdict

allowed = set(['AU','UA','CG','GC','GU','UG']) 
def kbest(s,k):
    def tryadd_binary(split,index1,index2):
        if index1 < len(opt[i,split-1]) and index2 < len(opt[split+1, j-1]) and not(split, index1,index2) in used:
            used.add(split, index1, index2)
            heappush(heap,(-(opt[i,split-1][index1][0]+ opt[split+1,j-1][index2][0] + 1), split, index1, index2))

    def tryadd_unary(index):
        if index < len(opt[i, j-1]):
            heappush(heap,(-(opt[i, j-1][index][0],index)))

    n = len(s)
    opt = defaultdict(list)
    heap = []
    used = set()

    for i in range(n):
        opt[i,i] = ([0,'.'])
        opt[i,i+1] = ([0,''])
    
    for span in range(2, n+1):
        for i in range(n-span+1):
            j = i+span-1

    for m in range(i,j):
        if (s[m]+s[j]) in allowed :
            tryadd_binary(m,0,0)
        tryadd_unary(0)

    uniq = set()
    for _ in range(k):
        if heap == []:
            break
        item = heappop(heap)
        if len(item) == 2:
            value, index = item
            opt[i,j].append(-value,'%s.' %(opt[i, j-1][index][1]))
            tryadd_unary(index+1)
        else:
            value, split, index1, index2 = item
            opt[i,j].append(-value,'%s(%s)' %((opt[i, split-1][index1][1]+opt[split+1,j-1][index2][1])))
            tryadd_binary(split, index1+1, index2)
            tryadd_binary(split,index1,index2+1)
    return opt[0,n-1]