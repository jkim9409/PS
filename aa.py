# # from typing import Optional
# #
# # class ListNode:
# #     def __init__(self,var,next):
# #         self.var = var
# #         self.next = next
# #
# #
# #
# # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# #
# # def mergeTwoLists(self, l1,l2)
# #self.node
#
#
# # class Node():
# #     def __init__(self, val, next=None):
# #         self.val = val
# #         self.next = next
# #
# # class MyCircularQueue:
# #     def __init__(self, k: int):
# #         self.num = k
# #         self.front = None
# #         self.end = None
# #         self.len = 0
# #
# #     def enQueue(self, val: int) -> bool:
# #         if self.len == self.num:
# #             return False
# #
# #         if not self.front:
# #             self.front = Node(val)
# #             self.front.next = self.front
# #             self.end = self.front
# #             self.len += 1
# #             return True
# #
# #         node = self.front
# #         while node.next != self.end:
# #             node = node.next
# #
# #         self.end = Node(val)
# #         node.next.next = self.end
# #         self.end.next = self.front
# #         self.len += 1
# #         return True
# #
# #     def deQueue(self) -> bool:
# #         if self.len == 0:
# #             return False
# #
# #         node = self.front.next
# #         self.end.next = node
# #         self.front = node
# #         self.len -= 1
# #         if self.len == 0:
# #             self.front = None
# #             self.end = None
# #
# #         return True
# #
# #     def Front(self) -> int:
# #         if self.len == 0:
# #             return -1
# #         return self.front.val
# #
# #     def Rear(self) -> int:
# #         if self.len == 0:
# #             return -1
# #         return self.end.val
# #
# #     def isEmpty(self) -> bool:
# #         return self.len == 0
# #
# #     def isFull(self) -> bool:
# #         return self.len == self.num
# #
# # a = MyCircularQueue(5)
# # print(a.enQueue(10))
# # print(a.enQueue(20))
# # print(a.enQueue(30))
# # print(a.enQueue(40))
# # print(a.Rear())
# # print(a.isFull())
# # print(a.deQueue())
# # print(a.deQueue())
# # print(a.enQueue(50))
# # print(a.enQueue(60))
# # print(a.Rear())
# # print(a.Front())
#
#
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
#                     grid[nx][ny] = '0'  # 스택에 쌓인 모든 친구들을 1 에서 0 으로 바꿔준다다
#     return cnt
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
#
# print(island_dfs_stack(grid))


n = 6
n = int(input())
for i in range(n:-1:-1):
    for j in range(n:-1:-1):
        print((i,j),end=' ')

    print()