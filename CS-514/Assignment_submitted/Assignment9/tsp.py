from collections import defaultdict
def tsp(n, edges):
    start_node = 0
    weight = defaultdict(lambda: 1 << 32)
    edge = defaultdict(set)
    
    for (u,v,w) in edges:
        weight[u,v] = weight[v,u] = min(w,weight[u,v]) 
        edge[u].add(v)
        edge[v].add(u)
    dist, arrow = defaultdict(lambda:1 << 32), defaultdict(lambda: -1)
    def distances(i, V):
        if (i, V) in dist: return dist[i,V], 0
        npush = 0
        for k in edge[i]:
            if (1<<k & V):
                lastDist = distances(k, V-(1<<k))
                dist1 = weight[i,k] + lastDist[0]
                npush += lastDist[1]
                if dist1 < dist[i,V]:
                    arrow[i, V] = k
                    dist[i,V] = dist1
                    npush += 1
        return dist[i,V], npush
        
    
    
    for u in range(1,n): 
        dist[u,0] = weight[u, start_node]
        arrow[u, 0] = start_node
    
    V = (1<<n)-2            
    resdistances, npush = distances(0, V)  
    Next, V, res = start_node, V+1, []
    while Next != -1:
        res.append(Next)
        V -= (1<<Next)
        Next = arrow[Next, V]
    return resdistances, res



print(tsp(2, [(0, 1, 1)]))
print(tsp(3, [(0, 1, 1), (1, 2, 2), (0, 2, 3)]))
print(tsp(4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)]))
print(tsp(4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6), (3, 0, 1)]))
print(tsp(11, [(0, 1, 29), (0, 2, 20), (0, 3, 21), (0, 4, 16), (0, 5, 31), (0, 6, 100), (0, 7, 12), (0, 8, 4),
                       (0, 9, 31), (0, 10, 18),
                       (1, 2, 15), (1, 3, 29), (1, 4, 28), (1, 5, 40), (1, 6, 72), (1, 7, 21), (1, 8, 29), (1, 9, 41),
                       (1, 10, 12),
                       (2, 3, 15), (2, 4, 14), (2, 5, 25), (2, 6, 81), (2, 7, 9), (2, 8, 23), (2, 9, 27), (2, 10, 13),
                       (3, 4, 4), (3, 5, 12), (3, 6, 92), (3, 7, 12), (3, 8, 25), (3, 9, 13), (3, 10, 25),
                       (4, 5, 16), (4, 6, 94), (4, 7, 9), (4, 8, 20), (4, 9, 16), (4, 10, 22),
                       (5, 6, 95), (5, 7, 24), (5, 8, 36), (5, 9, 3), (5, 10, 37),
                       (6, 7, 90), (6, 8, 101), (6, 9, 99), (6, 10, 84),
                       (7, 8, 15), (7, 9, 25), (7, 10, 13),
                       (8, 9, 35), (8, 10, 18),
                       (9, 10, 38)]))