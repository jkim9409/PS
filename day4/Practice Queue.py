from collections import deque
# class Node:
#     def __init__(self,val,next):
#         self.val = val
#         self.next = next
#
# class Queue:
#     def __init__(self):
#         self.front = None
#     def push(self,val):
#         if not self.front:
#             self.front = Node(val,None)
#             return
#         node = self.front
#         while node.next:
#             node = node.next
#         node.next = Node(val,None)
#     def pop(self):
#         if not self.front:
#             return None
#         node = self.front
#         self.front = node.next
#         return node.val

# n = 8
# q = Queue()
# i = 1
# while i <= n:
#     q.push(i)
#     i += 1
#
# while q.front.next:
#     q.pop()
#     if not q.front.next:
#         print(q.front.val)
#         break
#
#     add = q.pop()
#     node = q.front
#     while node.next:
#         node = node.next
#     node.next = Node(add,None)

#
# a = [2,5,1,2,3,4,5,6,7,8,9]
# q = deque(a)
# for i,val in enumerate(q):
#     print(i, val)
# for i in


class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):



