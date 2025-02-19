from collections import defaultdict
def tsp(n, edges):
    start_node = 0
    weight = defaultdict(lambda: 1 << 32)
    distance_dict = defaultdict(lambda: 1 << 32)
    side = defaultdict(set)
    
    for (to,frm,len) in edges: 
        weight[to,frm] = weight[frm,to] = min(len,weight[to,frm]) 
        side[to].add(frm)
        side[frm].add(to)

    
    key = defaultdict(lambda: -1)
    
    
    def distances(a, B):
        if (a, B) in distance_dict: return distance_dict[a, B], 0
        kpush = 0
        for k in side[a]:
            if (1<<k & B):
                lastDist = distances(k, B-(1<<k))
                dist1 = weight[a,k] + lastDist[0]
                kpush += lastDist[1]
                if dist1 < distance_dict[a, B]:
                    key[a, B] = k
                    distance_dict[a,B] = dist1
                    kpush += 1
        return distance_dict[a,B], kpush
        
    
    
    for u in range(1,n): 
        distance_dict[u,0] = weight[u, start_node]
        key[u, 0] = start_node
    
    V = (1<<n)-2            
    resdistances, kpush = distances(0, V)  
    Next, V, res = start_node, V+1, []
    while Next != -1:
        res.append(Next)
        V -= (1<<Next)
        Next = key[Next, V]
    return resdistances, res



print(tsp(2, [(0, 1, 1)]))
