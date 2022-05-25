# https://leetcode.com/problems/invert-binary-tree/
# Given the root of a binary tree, invert the tree, and return its root.
#
# Ex1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#
# Ex2:
# Input: root = [2,1,3]
# Output: [2,3,1]


def invertTree_pythonic(root):
    if root:
        root.left,root.rigjt = \
            invertTree_pythonic(root.right),invertTree_pythonic(root.left)
        return root
    return None


import collections
def invertTree_bfs(root):
    q = collections.deque([root])
    while q:
        node = q.popleft()
        if node:
            node.left,node.right = node.right, node.left

            q.append(node.left)
            q.append(node.right)
    return root

def invertTree_dfs(root):
    stack = collections([root])

    while stack:
        node = stack.pop()

        if node:
            node.left,node.right = node.right,node.left

            stack.append(node.left)
            stack.append(node.right)

    return root

def invertTree_postorder(root):
    stack = collections.deque([root])

    while stack:
        node = stack.pop()
        if node:
            stack.append(node.left)
            stack.append(node.right)

            node.left, node.right = node.right, node.left

    return root
