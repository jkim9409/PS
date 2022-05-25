# https://leetcode.com/problems/number-of-islands/
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Ex1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
# Ex2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# def island_dfs_stack(grid):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     rows, cols = len(grid), len(grid[0])
#     cnt = 0
#
#     for row in range(rows):
#         for col in range(cols):
#             if grid[row][col] != '1':
#                 continue
#
#             cnt += 1
#             stack = [(row, col)]
#
#             while stack:
#                 x, y = stack.pop()
#                 # grid[x][y] = '0' # 스택에 쌓인 모든 친구들을 1 에서 0 으로 바꿔준다다
#                 for i in range(4):
#                     nx = x + dx[i]
#                     ny = y + dy[i]
#                     if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
#                         continue
#                     stack.append((nx, ny))
#                     # grid[nx][ny] = '0'  # 스택에 쌓인 모든 친구들을 1 에서 0 으로 바꿔준다다
#     return cnt
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
#
# print(island_dfs_stack(grid))
# #------------------------------------------------------------------------------
# def island_dfs_recursive(grid):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     m = len(grid)
#     n = len(grid[0])
#     cnt = 0
#
#     def dfs_recursive(r, c):
#         if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
#             return
#
#         # 방문처리
#         grid[r][c] = '0'
#         for i in range(4):
#             dfs_recursive(r + dx[i], c + dy[i])
#         return
#
#     for r in range(m):
#         for c in range(n):
#             node = grid[r][c]
#             if node != '1':
#                 continue
#
#             cnt += 1
#             dfs_recursive(r, c)
#
#     return cnt


def numberofisland_mysolution(grid):

    count = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(r,c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        dfs(r+1,c)
        dfs(r,c+1)
        dfs(r-1,c)
        dfs(r,c-1)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1':
                count += 1
                dfs(row,col)

    return count


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]


print(numberofisland_mysolution(grid))