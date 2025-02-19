from collections import defaultdict, deque

def Max_Flow_Fat(input_data):
    source, sink, edges = input_data

    graph = defaultdict(list)
    for u, v, capacity in edges:
        graph[u].append((v, capacity))
        graph[v].append((u, 0))  # add reverse edges with 0 capacity

    flow_parents = {}
    max_flow = 0
    all_paths = defaultdict(lambda: defaultdict(int))

    while dfs(graph, source, sink, flow_parents):
        path_flow = float("inf")
        current_node = sink
        path = {}

        while current_node != source:
            parent_node = flow_parents[current_node]
            for neighbor, capacity in graph[parent_node]:
                if neighbor == current_node:
                    path_flow = min(path_flow, capacity)
                    path[parent_node] = current_node
                    break
            current_node = flow_parents[current_node]

        update_residual_capacities(graph, flow_parents, path_flow, source, sink)

        for node, child in path.items():
            all_paths[node][child] += path_flow

        max_flow += path_flow
        flow_parents = {}

    path_list = []
    for node in sorted(all_paths.keys()):
        for child in sorted(all_paths[node].keys()):
            path_list.append((node, child, all_paths[node][child]))

    return max_flow, path_list


def dfs(graph, source, sink, flow_parents):
    visited = set()
    queue = deque()
    queue.append(source)
    visited.add(source)

    while queue:
        parent = queue.popleft()
        for child, capacity in graph[parent]:
            if child not in visited and capacity > 0:
                queue.append(child)
                visited.add(child)
                flow_parents[child] = parent
    return sink in visited


def Max_Flow_Short(input_data):
    source, sink, edges = input_data

    graph = defaultdict(list)
    for u, v, capacity in edges:
        graph[u].append((v, capacity))
        graph[v].append((u, 0))

    flow_parents = {}
    max_flow = 0
    all_paths = defaultdict(lambda: defaultdict(int))

    while bfs(graph, source, sink, flow_parents):
        path_flow = float("inf")
        current_node = sink
        path = {}

        while current_node != source:
            parent_node = flow_parents[current_node]
            for neighbor, capacity in graph[parent_node]:
                if neighbor == current_node:
                    path_flow = min(path_flow, capacity)
                    path[parent_node] = current_node
                    break
            current_node = flow_parents[current_node]

        for node, child in path.items():
            all_paths[node][child] += path_flow

        update_residual_capacities(graph, flow_parents, path_flow, source, sink)

        max_flow += path_flow
        current_node = sink
        while current_node != source:
            parent_node = flow_parents[current_node]
            update_residual_capacities(graph, flow_parents, path_flow, parent_node, current_node)
            current_node = flow_parents[current_node]

    path_list = []
    for node in sorted(all_paths.keys()):
        for child in sorted(all_paths[node].keys()):
            path_list.append((node, child, all_paths[node][child]))

    return max_flow, path_list


def bfs(graph, source, sink, flow_parents):
    visited = set()
    queue = deque()
    queue.append(source)
    visited.add(source)

    while queue:
        current_node = queue.popleft()
        for neighbor, capacity in graph[current_node]:
            if neighbor not in visited and capacity > 0:
                queue.append(neighbor)
                visited.add(neighbor)
                flow_parents[neighbor] = current_node
                if neighbor == sink:
                    return True
    return False


def update_residual_capacities(graph, flow_parents, path_flow, from_node, to_node):
    for i, (vertex, capacity) in enumerate(graph[from_node]):
        if vertex == to_node:
            graph[from_node][i] = (vertex, capacity - path_flow)
            break

    for i, (vertex, capacity) in enumerate(graph[to_node]):
        if vertex == from_node:
            graph[to_node][i] = (vertex, capacity + path_flow)
            break


if __name__ == "__main__":
    print(Max_Flow_Short((0, 3, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])))
