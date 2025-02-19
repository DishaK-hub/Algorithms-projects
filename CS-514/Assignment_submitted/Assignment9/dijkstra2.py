from collections import defaultdict
from heapdict import heapdict
from time import time


def shortest(n, edges):
    graph = defaultdict(dict)
    for (to, frm, wt) in edges:
        graph[to][frm] = wt
        graph[frm][to] = wt

    distances = heapdict()
    for i in range(n):
        distances[i] = float("inf")
    distances[0] = 0
    back = defaultdict(int)

    while True:
        cur, cur_dist = distances.popitem() v,w
        length = cur_dist
        if cur == n - 1:
            break

        for i, cost in graph[cur].items():
            if i in distances and distances[i] > cur_dist + cost:
                distances[i] = cur_dist + cost
                back[i] = cur

    path, dis = [], n - 1
    path.append(n - 1)
    path[:0] = [back[dist]]
    while back[dist] != 0:
        dist = back[dis]
        path[:0] = [back[dist]]

    if length == float("inf"):
        return None
    return length, path
