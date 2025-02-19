import heapq

def _nbestc(a, b):
    def put(i, j):
        if 0 <= i < n and 0 <= j < n and (i, j) not in used:
            used.add((i, j))
            heapq.heappush(h, ((sa[i]+sb[j], sb[j]), (sa[i], sb[j]), (i, j))) # decorate: cmp_key, pair, index
        
    sa, sb = sorted(a), sorted(b)
    n = len(a)
    h, used = [], set()

    put(0, 0)
    for _ in range(n):
        _, xy, (i, j) = heapq.heappop(h)
        yield xy
        put(i+1, j)
        put(i, j+1)

nbestc = lambda a, b: list(_nbestc(a, b))

if __name__ == "__main__":
    a, b = [4,1,5,3], [2,6,3,4]
    #print(nbesta(a,b))
    #print(nbestb(a,b))
    print(nbestc(a,b))