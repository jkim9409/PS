# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Ex1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
# Ex2:
# Input: root = [1,null,2]
# Output: 2

from collections import deque
class TreeNode:
    def __init__(self,val,left= None,right= None):
        self.val = val
        self.left = left
        self.right = right

def maketree(lst,index):
    if index >= len(lst):
        return
    if lst[index] is None:
        return

    parent = TreeNode(lst[index])
    parent.left = maketree(lst,index*2+1)
    parent.right = maketree(lst,index*2+2)

    return parent

def maxlenth(root):
    count = -1
    q = deque([root])
    while q:
        count += 1
        for _ in range(len(q)):
            cur = q.popleft()
            if cur:
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

    return count

def solution(lst):
    parent = maketree(lst,0)
    a = maxlenth(parent.left)
    b = maxlenth(parent.right)
    max_len = a+b +1

    return max_len

print(solution([1,2,3,4,5]))