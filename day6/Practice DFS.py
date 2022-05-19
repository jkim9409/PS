# def dfs_stack(graph,start):
#     visited = []
#     stack = [start]
#     while stack:
#         top = stack.pop()
#         visited.append(top)
#         for adj in graph[top]:
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