import queue
import time

def MST_Prim(graph):
    min_spanning_tree = {}
    visited = set()
    priority_queue = queue.PriorityQueue()
    result_weight = 0
    result_list = []

    for x in graph:
        start, end, weight = x
        if start not in min_spanning_tree:
            min_spanning_tree[start] = list()
        if end not in min_spanning_tree:
            min_spanning_tree[end] = list()
        min_spanning_tree[start].append((start, end, weight))
        min_spanning_tree[end].append((end, start, weight))
    visited.add(0)
    for x in min_spanning_tree[0]:
        start, end, weight = x
        priority_queue.put((weight, start, end))
    while not priority_queue.empty():
        weight, start, end = priority_queue.get()
        if end not in visited:
            result_weight += weight
            result_list.append((min(start, end), max(start, end)))
            visited.add(end)
            for x in min_spanning_tree[end]:
                priority_queue.put((x[2], x[0], x[1]))

    return (result_weight, result_list)

def MST_Kruskal(graph):
    def find(parent, node):
        if parent[node] == node:
            return node
        return find(parent, parent[node])

    def union(parent, rank, u, v):
        root_u = find(parent, u)
        root_v = find(parent, v)
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

    graph.sort(key=lambda x: x[2])

    min_spanning_tree = set()
    parent = {}
    rank = {}

    for u, v, weight in graph:
        if u not in parent:
            parent[u] = u
            rank[u] = 0
        if v not in parent:
            parent[v] = v
            rank[v] = 0

        if find(parent, u) != find(parent, v):
            min_spanning_tree.add((u, v, weight))
            union(parent, rank, u, v)

    total_weight = sum(weight for _, _, weight in min_spanning_tree)
    min_spanning_tree.discard((0, 0, 0))
    result_list = [(t[0], t[1]) for t in min_spanning_tree]

    return (total_weight, result_list)

