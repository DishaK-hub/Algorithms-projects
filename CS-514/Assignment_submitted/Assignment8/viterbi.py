from collections import defaultdict

def order(n, edges):

    array1 = [0] * n
    t_order = []
    graph = defaultdict(list)

    for (u, v) in edges:
        array1[v] += 1
        graph[u].append(v)
    list1 = []
    m = 0

    for i in range(n):
        if array1[i] == 0:
            list1.append(i)

    while m != len(list1):
        i = list1[m]
        t_order.append(i)
        m += 1

        adj = graph[i]


        for j in adj:
            array1[j] -= 1
            if array1[j] == 0:
                list1.append(j)

    if (len(t_order)!= n):
        return None

    return t_order


def longest(n, edges):

    array1 = [0] * n
    array2 = [0] * n
    array3 = [0] * n
    

    graph = defaultdict(list)

    for (u, v) in edges:
        array1[v] += 1
        graph[v].append(u)

    t_order = order(n, edges)

    max_dg = 0
    max_v = 0

    for i in t_order:
        if array1[i] != 0:
            adj = graph[i]

            for v in adj:
                if array3[i] < array3[v] + 1:
                    array3[i] = array3[v] + 1
                    array2[i] = v
                    
            if array3[i] > max_dg:
                max_dg = array3[i]
                max_v = i
    v = max_v
    longest_path = []
    longest_path.append(v)

    while array1[v] != 0:
        v = array2[v]
        longest_path[:0] = [v]

    return max_dg, longest_path


print(longest(8,[(0, 1),(0, 2),(1, 2),(2, 3),(2, 4),(4, 3),(3, 5),(4, 5),(5, 6),(5, 7),(6, 7),],))