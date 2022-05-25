# from collections import deque
#
# class TreeNode:
#     def __init__(self,val,left =None, right =None):
#         self.val = val
#         self.left = left
#         self.right =right
#
#
# def maketree(lst,index):
#     if index > len(lst):
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
# def max_depth(lst):
#     if not lst:
#         return 0
#     root = maketree(lst,0)
#     q = deque([root])
#     depth = 0
#     while q:
#         depth += 1
#         for _ in range(len(q)):
#             cur = q.popleft()
#             if cur.left:
#                 q.append(cur.left)
#             if cur.right:
#                 q.append(cur.right)
#
#     return depth
#
#
# print(max_depth([3, 9, 20, None, None, 15, 7]))

#------------------------------------------------------------------


from collections import deque
class TreeNode:
    def __init__(self,val,left= None,right= None):
        self.val = val
        self.left = left
        self.right = right

def make_tree_by(lst,idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value is None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2*idx +1)
        parent.right = make_tree_by(lst, 2*idx +2)

    return parent

def test_max_depth(lst):
    root = make_tree_by(lst,0)
    if not root:
        return 0

    q = deque([root])
    depth = 0

    while q:
        depth += 1

        for _ in range(len(q)):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    return depth

print(test_max_depth([3, 9, 20, None, None, 15, 7]))