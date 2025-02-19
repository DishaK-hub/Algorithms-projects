from collections import defaultdict
def __order3(n,edges):
    adjlist = defaultdict(list)
    indegree = defaultdict(int)

    for u,v in edges:
        adjlist[u].append(v)
        indegree[v]+=1

    stack = [u for u in range(n) if indegree[u]==0]

    while stack!=[]:
        u = stack.pop()
        yield u
        for v in adjlist[u]:
            indegree[v]-=1
            if indegree[v] == 0:
                stack.append(v)

def order(n,edges):
    out = list(__order3(n,edges))
    return out if len(out) == n else None

print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
