# https://leetcode.com/problems/balanced-binary-tree/
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
# Ex1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Ex2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

def isBalanced(root):
    def check(root):
        if not root:
            return 0

        left = check(root.left)
        right = check(root.right)

        if left == -1 or \
                right == -1 or \
                abs(left - right) > 1:
            return -1
        return max(left,right) + 1

    return check(root) != -1


