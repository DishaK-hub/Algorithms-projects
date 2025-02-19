from collections import defaultdict

def order(n,edges):

    def visit(v):
        if v in visited:
            return

        visited.add(v)
        for u in prereqs[v]:
            visit(u)

        output.append(v)

    graph = defaultdict(list)
    prereqs =  defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        prereqs[v].append(u)

    nodes = range(n)
    output = []
    visited = set()
    for v in nodes:
        visit(v)

    return output


print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
#    [0, 1, 2, 3, 4, 5, 6, 7]

print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
#    [0, 1, 2, 4, 3, 5, 6, 7]

#    If there is a cycle, return None

print(order(4, [(0,1), (1,2), (2,1), (2,3)]))
#    None

#    Other cases:

print(order(5, [(0,1), (1,2), (2,3), (3,4)]))
#    [0, 1, 2, 3, 4]

print(order(5, []))
#    [0, 1, 2, 3, 4]  # could be any order   

print(order(3, [(1,2), (2,1)]))
#    None

print(order(1, [(0,0)])) # self-loop
#    None