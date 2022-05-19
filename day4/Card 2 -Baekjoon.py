#https://www.acmicpc.net/problem/2164
# input: 6
# output: 4



class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
    def push(self,val):
        if not self.front:
            self.front = Node(val,None)
            return
        node = self.front
        while node.next:
            node = node.next
        node.next = Node(val,None)
    def pop(self):
        if not self.front:
            return None
        node = self.front
        self.front = node.next
        return node.val

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

from collections import deque
# def card_lecture_solution (num):
#     deq = deque([i for i in range(1, num+1)])
#     while len(deq) > 1:
#         deq.popleft()
#         deq.append(deq.popleft())
#     return deq.popleft()
#
# print(card_lecture_solution(6))
#https://wiki.python.org/moin/TimeComplexity
a = deque([1])
a.popleft()
print(a)