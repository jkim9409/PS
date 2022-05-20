# def dfs_stack(graph,start):
#     visited = []
#     stack = [start]
#     while stack:
#         top = stack.pop()
#         visited.append(top)
# #         for adj in graph[top]:
#             if adj not in visited:
#                 stack.append(adj)
#
#     return visited
#
# graph = {
#     1: [2, 3, 4],
#     2: [5],
#     3: [5],
#     4: [],
#     5: [6, 7],
#     6: [],
#     7: [3],
# }
# start = 1
# print(dfs_stack(graph, start))
#-------------------------------------------------------------------

def dfs_recursive(node,visited,graph):
    visited.append(node)
    for adj in graph[node]:
        if adj not in visited:
            dfs_recursive(adj,visited,graph)
    return visited

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}
node = 1
visited = []
print(dfs_recursive(node, visited ,graph))
#------------------------------------------------------------------------------------
from collections import deque

N, L, S = map(int, input().split())
grid = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(L):
    x, y = map(int, input().split())
    grid[x][y] = grid[y][x] = 1

visit = []
visit_bfs = []
stack = [S]
result = []
deq = deque([S])
while stack:
    # 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
    top = stack.pop()
    if top in visit:
        continue
    print(top, end=' ')
    visit.append(top)
    for i in reversed(range(1, N + 1)):
        if grid[top][i] == 1:
            stack.append(i)
# 방문할 노드가 남아있는 한 아래 로직을 반복한다.
print()
while deq:
    # 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
    top = deq.popleft()
    if top in visit_bfs:
        continue
    print(top, end=' ')
    visit_bfs.append(top)
    for i in range(1, N + 1):
        if grid[top][i] == 1:
            deq.append(i)

def combinations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combinations(array[i+1:], r-1):
                yield [array[i]] + next