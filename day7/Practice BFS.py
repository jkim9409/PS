from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def bfs_queue(start):
    q = deque([start])
    visited = [start]
    while q:
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:
                visited.append(adj)
                q.append(adj)

    return visited

def dfs_stack(start):
    stack = [start]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node)
        for adj in graph[node]:
            if adj not in visited:
                stack.append(adj)
    return visited

def dfs_recursive(start,visited = []):
    visited.append(start)
    for adj in graph[start]:
        if adj not in visited:
            dfs_recursive(adj,visited)
    return visited


print(bfs_queue(1))
print(dfs_stack(1))
print(dfs_recursive(1))