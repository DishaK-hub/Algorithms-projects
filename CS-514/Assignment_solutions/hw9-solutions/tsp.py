#!/usr/bin/env python3

from collections import defaultdict
import time
from heapdict import heapdict # SLOW
from priority_dict import priority_dict # FAST
from pqdict import pqdict
from heapq import heappush, heappop

INFTY = float("inf")

def tsp(n, _edges): # the Viterbi implementation

    def backtrace(i, nodeset, j):
        if j == 0:
            return [0]
        _, last = best[i][nodeset, j]
        newset = nodeset - frozenset([j])
        return backtrace(i-1, newset, last) + [j%n]

    start_time = time.time()

    edges = defaultdict(lambda : defaultdict(lambda : INFTY))
    for (u,v,c) in _edges:
        edges[u][v] = min(edges[u][v], c) # possible duplicate edges
        edges[v][u] = min(edges[v][u], c) # undirected
    for u in range(1,n): # clone a special sink n from 0
        edges[u][n] = edges[u][0] 
        
    best = [defaultdict(lambda : (float("inf"), None)) for _ in range(n+2)] # best and back together
    best[1][frozenset([0]), 0] = (0, None)
    pushes = pops = 0
    for i in range(1,n+1): #i->i+1
        for (nodeset, last), (value, _) in best[i].items():
        #for nodeset, last in best[i]:
            #value = best[i][nodeset, last]
            pops += 1
            for j in range(1,n) if i < n else [n]:
                if j in edges[last] and j not in nodeset:
                    newvalue = value + edges[last][j]
                    newset = nodeset | frozenset([j])
                    if newvalue < best[i+1][newset, j][0]:
                        pushes += 1
                        best[i+1][newset, j] = (newvalue, last)

    fullsetplus = frozenset(range(n+1)) # all nodes from 0 to n
            
    print("Viterbi, set, time: %.2f" % (time.time() - start_time), "pushes:", pushes, "pops:", pops)
    return (best[n+1][fullsetplus, n][0], backtrace(n+1, fullsetplus, n))    

def tsp_bit(n, _edges): # the Viterbi implementation

    def backtrace(i, nodeset, j):
        if j == 0:
            return [0]
        _, last = best[i][nodeset, j]
        return backtrace(i-1, nodeset - (1 << j), last) + [j%n] # unset j bit 

    start_time = time.time()

    edges = defaultdict(lambda : defaultdict(lambda : float("inf")))
    for (u,v,c) in _edges:
        edges[u][v] = min(edges[u][v], c) # possible duplicate edges
        edges[v][u] = min(edges[v][u], c) # undirected
    for u in range(1,n): # clone a special sink n from 0
        edges[u][n] = edges[u][0]
        
    best = [defaultdict(lambda : (INFTY, None)) for _ in range(n+2)] # best and back together
    best[1][1, 0] = (0, None) # 1: 000001
    pushes = pops = 0
    for i in range(1,n+1): #i->i+1
        for (nodeset, last), (value, _) in best[i].items():
        #for nodeset, last in best[i]:
            #value = best[i][nodeset, last]
            pops += 1
            for j in range(1,n) if i < n else [n]:
                if j in edges[last] and not (1<<j & nodeset): # query j'th bit
                    newvalue = value + edges[last][j] 
                    newset = nodeset | (1<<j) # set j'th bit
                    if newvalue < best[i+1][newset, j][0]:
                        pushes += 1
                        best[i+1][newset, j] = (newvalue, last)

    fullsetplus = (1 << (n+1)) - 1 # 2^{n+1}-1: 111...1: all nodes (0..n)
            
    print("Viterbi, bit, time: %.2f" % (time.time() - start_time), "pushes:", pushes, "pops:", pops)
    return (best[n+1][fullsetplus, n][0], backtrace(n+1, fullsetplus, n))

def tsp_dijk_bit_pqdict(n, _edges): # the Dijkstra implementation

    def backtrace(nodeset, j):
        if nodeset == 1:
            return [0]
        last = back[nodeset, j]
        return backtrace(nodeset - (1<<j), last) + [j%n]

    start_time = time.time()

    edges = defaultdict(lambda : defaultdict(lambda: INFTY))
    for (u,v,c) in _edges:
        edges[u][v] = min(edges[u][v], c) # possible duplicate edges
        edges[v][u] = min(edges[v][u], c) # undirected
    for u in range(1,n): # Matthew's suggestion: clone a special sink n from 0
        edges[u][n] = edges[u][0] 
        
    queue = priority_dict() # pqdict() # heapdict() #priority_dict() #heapdict()
    queue[1, 0] = 0
    back = {}
    popped = set() # black nodes
    best = defaultdict(lambda: INFTY)

    pushes = pops = 0
    full, fullplus = (1<<n) - 1, (1<<(n+1))-1
    while queue:
        (nodeset, last), value = queue.popitem()
        popped.add((nodeset, last))
        pops += 1
        if nodeset == fullplus: # full set + [0]
            print("Dijkstra, bit, decrease-key, time: %.2f" % (time.time() - start_time), "pushes:", pushes, "pops:", pops)
            return (value, backtrace(nodeset, last))
            
        for j in range(1,n) if nodeset < full else [n]:
            if j in edges[last] and not (1<<j & nodeset):
                newvalue = value + edges[last][j]
                newset = nodeset | (1<<j)
                #if (newset, j) not in popped and \
                #   ((newset, j) not in queue or newvalue < queue[newset, j]): # N.B.: **not black** and (white or better)
                # important: needs to check "not black" because queue only contains gray nodes
                # print("push", newvalue, newset, j)
                if newvalue < best[newset, j]: # just checking if there is any improvement is enough
                    queue[newset, j] = newvalue # decrease-key
                    best[newset, j] = newvalue
                    back[newset, j] = last
                    pushes += 1

def tsp_dijk_bit_heapq(n, _edges): # the Dijkstra implementation

    def backtrace(nodeset, j):
        if nodeset == 1:
            return [0]
        last = back[nodeset, j]
        return backtrace(nodeset - (1<<j), last) + [j%n]

    start_time = time.time()

    edges = defaultdict(lambda : defaultdict(lambda : INFTY))
    for (u,v,c) in _edges:
        edges[u][v] = min(edges[u][v], c) # possible duplicate edges
        edges[v][u] = min(edges[v][u], c) # undirected
    for u in range(1,n): # Matthew's suggestion: clone a special sink n from 0
        edges[u][n] = edges[u][0] 
        
    queue = [(0, (1, 0))] # (value, (nodeset, last), back)
    popped = set()
    best = defaultdict(lambda : INFTY)
    back = {}
    pushes = pops = 0
    full, fullplus = (1<<n) - 1, (1<<(n+1)) - 1
    while queue != []:
        value, (nodeset, last) = heappop(queue)
        pops += 1
        if (nodeset, last) not in popped:
            popped.add((nodeset, last))
            if nodeset == fullplus: # full set + [0]
                print("Dijkstra, bit, heapq, time: %.2f" % (time.time() - start_time), "pushes:", pushes, "pops:", pops)
                return (value, backtrace(nodeset, last))    

            for j in range(1,n) if nodeset < full else [n]:
                if j in edges[last] and not ((1<<j) & nodeset):
                    newvalue = value + edges[last][j]
                    newset = nodeset | (1<<j)
                    #if (newset, j) not in fixed: # just checking "not black" is not optimal
                    if newvalue < best[newset, j]:
                        best[newset, j] = newvalue
                        back[newset, j] = last
                        heappush(queue, (newvalue, (newset, j)))
                        pushes += 1


if __name__ == "__main__":
    print (tsp_bit(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
    print (tsp_bit(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6), (3,0,1)]))
    # print (tsp_dijk(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6), (3,0,1)]))

    
    # map of germany: https://stackoverflow.com/questions/11007355/data-for-simple-tsp # dense graph!    
    germany = [(0,1,29),(0,2,20),(0,3,21),(0,4,16),(0,5,31),(0,6,100),(0,7,12),(0,8,4),(0,9,31),(0,10,18), 
               (1,2,15),(1,3,29),(1,4,28),(1,5,40),(1,6,72),(1,7,21),(1,8,29),(1,9,41),(1,10,12),
               (2,3,15),(2,4,14),(2,5,25),(2,6,81),(2,7,9),(2,8,23),(2,9,27),(2,10,13),
               (3,4,4),(3,5,12),(3,6,92),(3,7,12),(3,8,25),(3,9,13),(3,10,25),
               (4,5,16),(4,6,94),(4,7,9),(4,8,20),(4,9,16),(4,10,22),
               (5,6,95),(5,7,24),(5,8,36),(5,9,3),(5,10,37),
               (6,7,90),(6,8,101),(6,9,99),(6,10,84),
               (7,8,15),(7,9,25),(7,10,13),
               (8,9,35),(8,10,18),
               (9,10,38)]
    print("\nGermany graph...")
    print (tsp_bit  (11, germany))
    print (tsp_dijk_bit_pqdict (11, germany))
    print (tsp_dijk_bit_heapq (11, germany))

    print("\nRandom graph 1...")
    import random
    random.seed(2)
    n, m = 16, 1000
    edges = [(random.randint(0,n-1), random.randint(0,n-1), random.randint(10,300)) for _ in range(m)] + \
            [(random.randint(0,n-1), random.randint(0,n-1), random.randint(300,600)) for _ in range(m)] 
    #print (edges)


    print (tsp (n, edges)) # (11, [0, 4, 1, 3, 2, 0])
    print (tsp_bit (n, edges)) # (11, [0, 4, 1, 3, 2, 0])
    print (tsp_dijk_bit_pqdict (n, edges))
    print (tsp_dijk_bit_heapq (n, edges))

    print("\nRandom graph 2...")
    
    n, edges = 16, [(1, 2, 0), (11, 5, 5), (9, 8, 4), (6, 1, 4), (5, 13, 5), (12, 11, 4), (14, 8, 0), (0, 11, 3), (10, 12, 3), (5, 5, 1), (7, 0, 1), (10, 5, 1), (11, 5, 3), (13, 11, 4), (11, 11, 3), (5, 12, 5), (14, 7, 3), (8, 15, 4), (11, 14, 3), (11, 14, 3), (7, 10, 5), (5, 8, 3), (9, 9, 5), (13, 9, 5), (6, 15, 4), (11, 2, 2), (0, 6, 5), (3, 1, 4), (1, 8, 4), (7, 3, 4), (4, 8, 1), (6, 1, 3), (1, 1, 2), (11, 5, 1), (0, 2, 0), (2, 0, 0), (0, 11, 2), (4, 5, 5), (5, 0, 3), (1, 7, 1), (1, 0, 2), (3, 9, 2), (15, 0, 2), (14, 1, 2), (12, 4, 3), (7, 2, 5), (10, 3, 0), (14, 4, 4), (12, 15, 4), (10, 4, 2), (8, 8, 4), (13, 0, 5), (4, 1, 2), (1, 4, 1), (5, 3, 3), (7, 1, 1), (7, 14, 0), (8, 2, 4), (7, 11, 2), (13, 8, 4), (0, 4, 0), (12, 13, 1), (3, 2, 1), (3, 3, 0), (5, 7, 0), (6, 0, 4), (14, 14, 2), (12, 6, 5), (6, 13, 3), (0, 1, 3), (5, 3, 5), (15, 11, 0), (3, 11, 2), (11, 9, 0), (13, 3, 0), (9, 6, 5), (0, 14, 0), (13, 15, 3), (6, 2, 0), (9, 0, 2), (9, 2, 1), (15, 6, 0), (11, 12, 5), (14, 4, 2), (12, 3, 2), (3, 3, 0), (10, 12, 1), (3, 0, 4), (15, 1, 5), (15, 9, 2), (14, 4, 2), (8, 15, 4), (15, 13, 3), (9, 12, 1), (5, 15, 4), (8, 13, 5), (2, 3, 0), (11, 5, 4), (4, 13, 0), (2, 1, 1)]

    print (tsp (n, edges)) # (11, [0, 4, 1, 3, 2, 0])
    print (tsp_bit (n, edges)) # (11, [0, 4, 1, 3, 2, 0])
    print (tsp_dijk_bit_pqdict (n, edges))
    print (tsp_dijk_bit_heapq (n, edges))
