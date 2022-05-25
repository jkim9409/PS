# https://leetcode.com/problems/search-in-a-binary-search-tree/
#
# You are given the root of a binary search tree (BST) and an integer val.
#
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
#
# Ex1:
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
#
# Ex2:
# Input: root = [4,2,7,1,3], val = 5
# Output: []
#


class NodeTree:
    def __init__(self,val,left= None, right= None ):
        self.val = val
        self.left = left
        self.right = right

def maketree(lst,index):
    if index >= len(lst):
        return

    node = NodeTree(lst[index])
    node.left = maketree(lst,index*2+1)
    node.right = maketree(lst,index*2+2)

    return node

node = maketree([4,2,7,1,3],0)
# print(maketree([4,2,7,1,3],0))


def searchtree(tree,val):

    if tree is None:
        return None

    if tree.val == val:
        node = tree
        return

    node = None

    searchtree(tree.left, val)
    searchtree(tree.right, val)

    return node
searchtree(node,2)