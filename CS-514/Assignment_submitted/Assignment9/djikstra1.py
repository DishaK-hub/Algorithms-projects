from heapq import heapify, heappush, heappop

class priority_dict(dict):
    
    def __init__(self, *args, **kwargs):
        super(priority_dict, self).__init__(*args, **kwargs)
        self._rebuild_heap()

    def _rebuild_heap(self):
        self._heap = [(v, k) for k, v in self.items()] # lhuang: iteritems -> items
        heapify(self._heap)

    def smallest(self):
        heap = self._heap
        v, k = heap[0]
        while k not in self or self[k] != v:
            heappop(heap)
            v, k = heap[0]
        return k, v # lhuang: returns k, v instead of k

    def pop_smallest(self):
        heap = self._heap
        v, k = heappop(heap)
        while k not in self or self[k] != v:
            v, k = heappop(heap)
        del self[k]
        return k, v # lhuang: returns k, v not k

    popitem = pop_smallest # lhuang (to be consistent with heapdict); otherwise calls dict.popitem()

    def __setitem__(self, key, val):
        super(priority_dict, self).__setitem__(key, val)
        
        if len(self._heap) < 2 * len(self):
            heappush(self._heap, (val, key))
        else:
            self._rebuild_heap()

    def setdefault(self, key, val):
        if key not in self:
            self[key] = val
            return val
        return self[key]

    def update(self, *args, **kwargs):
        super(priority_dict, self).update(*args, **kwargs)
        self._rebuild_heap()

    def sorted_iter(self):
        while self:
            yield self.pop_smallest()

def shortest(n, edges, source=None, destination=None):

    if(source==None):
        source = 0
        if(destination==None):
            destination = n-1

    adj = [] 
    parent = []
    for i in range(n):
        adj.append([])
        parent.append(-1)
    print(adj)
    print(parent)
    for e in edges:
        adj[e[0]].append((e[1], e[2]))
        adj[e[1]].append((e[0], e[2]))
    print(adj)

    #h = heapdict()
    h = priority_dict()
    h[source] = 0
    parent[source] = source
    path = []

    while(len(h) > 0):

        v, d = h.popitem()

        if(v == destination): 
            path = [] 
            i = v
    while(i!=source):
        path.append(i)
        i = parent[i]
        path.append(source)
        path = path[::-1] 
        return d, path

    for e in adj[v]:
        if(parent[e[0]] == -1 or 
        (e[0] in h) and h[e[0]] > d+e[1] ):
            h[e[0]] = d+e[1]
            parent[e[0]] = v 
    return None



print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))