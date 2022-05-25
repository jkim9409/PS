# https://leetcode.com/problems/merge-two-binary-trees/
# You are given two binary trees root1 and root2.
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
# Return the merged tree.
# Note: The merging process must start from the root nodes of both trees.
#
# Ex1:
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
#
# Ex2:
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]

class TreeNode:
    def __init__(self,val,left= None,right= None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(t1,t2):
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        node.left = mergeTrees(t1.left + t2.left)
        node.right = mergeTrees(t1.right + t2.right)

        return node
    else:
        return t1 or t2

