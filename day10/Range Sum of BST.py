# https://leetcode.com/problems/range-sum-of-bst/
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
#
# Ex1:
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Ex2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
#
#







class NodeTree:
    def __init__(self,val,left= None, right= None ):
        self.val = val
        self.left = left
        self.right = right

def maketree(lst,index):
    if index >= len(lst):
        return
    if lst[index] is None:
        return
    node = NodeTree(lst[index])
    node.left = maketree(lst,index*2+1)
    node.right = maketree(lst,index*2+2)

    return node

node = maketree([10,5,15,3,7,13,18,1,None,6],0)
# print(maketree([4,2,7,1,3],0))

def searchtree(tree,val1,val2):
    sum = 0
    def recursive(tree,val1,val2):
        nonlocal sum
        if tree is None:
            return
        if tree.val <= val2 and tree.val >= val1:
            sum += tree.val

        recursive(tree.left, val1, val2)
        recursive(tree.right, val1, val2)

        return sum
    recursive(tree,val1,val2)
    return sum



print(searchtree(node,6,10))