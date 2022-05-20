# https://www.acmicpc.net/problem/1260
#
# Ex1:
# Input:
#         graph = {
#             1:[2,3,4],
#             2:[1,4],
#             3:[1,4],
#             4:[1,2,3]
#         }
#         start = 1
#
# Output: [1,2,4,3]
#         [1,2,3,4]
#
# Ex2:
# Input:
#         graph = {
#             5:[4,2],
#             1:[2],
#             3:[4,1],
#             2:[]
#             4:[]

#         }
#         start = 3
#
# Output: [3,1,2,5,4]
#         [3,1,4,2,5]

# Ex3:
# Input:
#         graph = {
#             999:[1000]
#             1000:[999]
#         }
#         start = 1
#
# Output: [1000, 999]
#         [999, 1000]

def dfs(graph, start):
    visited = [start]
    stack = [start]
    for key in graph:
        graph[key].sort(reverse=True)
    while stack:
        node = stack.pop()
        if node not in visited:
                visited.append(node)
        for adj in graph[node]:
            if adj not in visited:
                stack.append(adj)
    return visited

from collections import deque

def bfs(graph,start):
    visited = [start]
    q = deque([start])

    for key in graph:
        graph[key].sort()

    while q:
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)

    return visited


graph1 = {
    5:[4,2],
    1:[2,3],
    3:[4,1],
    2:[5,1],
    4:[5,3]
}
start1 = 3

graph2 = {
    1:[2,3,4],
    2:[1,4],
    3:[1,4],
    4:[1,2,3]
}
start2 = 1

graph3 = {
    999:[1000],
    1000:[999]
}
start3 = 1000

print(dfs(graph1,start1))
print(dfs(graph2,start2))
print(dfs(graph3,start3))

print(bfs(graph1,start1))
print(bfs(graph2,start2))
print(bfs(graph3,start3))

