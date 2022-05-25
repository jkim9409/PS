# https://leetcode.com/problems/diameter-of-binary-tree/
# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.
#
# Ex1:
# Input: root = [1,2,3,4,5]
# Output: 3
#
# Ex2:
# Input: root = [1,2]
# Output: 1


class Solution:
    longest = 0

    def diameterOfBinaryTree(self,root):
        def dfs(node):
            if not node:
                return -1

            #왼쪽, 오른쪽의 각 리프 노드까지 탐색한다.
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest  = max(self.longest,left + right + 2)

            return max(left,right) + 1

        dfs(root)
        return self.longest












# from collections import deque
# class TreeNode:
#     def __init__(self,val,left= None,right= None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# def maketree(lst,index):
#     if index >= len(lst):
#         return
#     if lst[index] is None:
#         return
#
#     parent = TreeNode(lst[index])
#     parent.left = maketree(lst,index*2+1)
#     parent.right = maketree(lst,index*2+2)
#
#     return parent
#
# def maxlenth(root):
#     count = -1
#     q = deque([root])
#     while q:
#         count += 1
#         for _ in range(len(q)):
#             cur = q.popleft()
#             if cur:
#                 if cur.left:
#                     q.append(cur.left)
#                 if cur.right:
#                     q.append(cur.right)
#
#     return count
#
# def solution(lst):
#     parent = maketree(lst,0)
#     max_len = a = b = 0
#     if parent.left:
#         max_len +=1
#         a = maxlenth(parent.left)
#     if parent.right:
#         max_len +=1
#         b = maxlenth(parent.right)
#
#     max_len = a+b +max_len
#
#     return max_len
#
# print(solution([1,2]))