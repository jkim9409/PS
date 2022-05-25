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

# from collections import deque
#
# def island_bfs(grid):
#     rows,cols = len(grid),len(grid[0])
#     count = 0
#
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#
#     for row in range(rows):
#         for col in range(cols):
#             if grid[row][col] == '0':
#                 continue
#
#             count += 1
#             q = deque([(row,col)])
#             while q:
#                 x,y = q.popleft()
#                 # grid[x][y] = '0'
#                 for i in range(4):
#                     nx = x + dx[i]
#                     ny = y + dy[i]
#                     if nx < 0 or nx >=rows or ny < 0 or ny >= cols or grid[nx][ny] == '0':
#                         continue
#
#                     grid[x][y] = '0'
#                     q.append((nx,ny))
#
#     return count

# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
#
# print(island_bfs(grid))
#

import collections

def numberofisland_queue(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1':
                q = collections.deque([(row,col)])

                count += 1
                while q:
                    x,y = q.popleft()
                    grid[x][y] = '0'
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] == '0':
                            continue
                        grid[nx][ny] = '0'
                        q.append((nx,ny))








    return count







grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numberofisland_queue(grid))
