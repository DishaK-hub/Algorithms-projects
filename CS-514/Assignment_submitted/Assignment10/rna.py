from collections import defaultdict
from heapq import heapify, heappop, heappush
basePairs = ['AU','GC','GU','UA','CG','UG']
    
def best(seq_string):

    def update_opt(i, j, w, scan):
        if w > opt[i, j]:
            opt[i, j] = w
            back[i, j] = scan
    #rnaset = ['AU','CG','GC','GU','UA','UG']
    def subproblem(i, j):
        if i == j: 
            return ""
        elif i == j-1:
            return "."
        k = back[i, j]
        if k == -1: 
            return "(" + subproblem(i+1, j-1) + ")"
        return subproblem(i, k) + subproblem(k, j)

    slen = len(seq_string)
    opt =  defaultdict(lambda : -1)
    back = {}
    for v in range(slen):
        opt[v, v+1],opt[v, v]  = 0,0
    
    for t in range(2, slen+1): 
        for i in range(slen-t+1): 
            j = i+t 
            
            if seq_string[i]+seq_string[j-1] in basePairs: 
                update_opt(i, j, opt[i+1, j-1] + 1, -1)
            for k in range(i+1, j): 
                update_opt(i, j, opt[i, k] + opt[k, j], k)
            
    return opt[0, slen], subproblem(0, slen)

def total(seq_string):
    
    slen = len(seq_string)
    final = defaultdict(int)
    #rnaset = ['AU','CG','GC','GU','UA','UG']

    for u in range(slen+1):
        final[u, u+1],final[u, u]  = 1 ,1

    for v in range(2, slen+1):
        for i in range(slen-v+1):
            j = i+v 
            
            final[i, j] += final[i+1, j] 

            for w in range(i+1, j+1):
                if seq_string[i]+seq_string[w-1] in basePairs:
                    final[i, j] += final[i+1, w-1] * final[w, j]

    return final[0, slen]

def kbest(seq_string, k):
   
    def try_push(p, u, v):
        if u < len(opt[i, p]) and v < len(opt[p, j]) \
           and not (p, u, v) in used:
            used.add((p, u, v))
            heappush(heap, 
                     (-opt[i, p][u][0]-opt[p, j][v][0], p, u, v))

    def try_pushdp(w):
        if w < len(opt[i+1, j-1]):
            heappush(heap, (-opt[i+1, j-1][w][0]-1, w))

    def add_value(value, str_scan):
        if str_scan not in distinct_set:
            opt[i, j].append((-value, str_scan)) 
            distinct_set.add(str_scan)

    best_seq = len(seq_string)
    opt = defaultdict(list)
    for i in range(best_seq):
        opt[i, i] = [(0, '')]
        opt[i, i+1] = [(0, '.')] 
        

    for t in range(2, best_seq+1): 
        for i in range(best_seq-t+1): 
            j = i+t

            heap = []            
            used = set()

            if seq_string[i]+seq_string[j-1] in basePairs: 
                try_pushdp(0)
            for t2 in range(i+1, j):
                try_push(t2, 0, 0)

            heapify(heap)
            distinct_set = set() 

            while heap != [] and len(opt[i, j]) < k:
                top_element = heappop(heap)
                if len(top_element) == 2: 
                    val, idx = top_element
                    add_value(val,"("+opt[i+1,j-1][idx][1]+")")
                    try_pushdp(idx+1)
                else: 
                    val, p, idx1, idx2 = top_element
                    add_value(val,(opt[i, p][idx1][1]+opt[p, j][idx2][1]))
                    try_push(p, idx1+1, idx2)
                    try_push(p, idx1, idx2+1)

    return opt[0,best_seq]



print(kbest("ACAGU", 3))
