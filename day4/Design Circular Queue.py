# class MyCircularQueue:
#     def __init__(self,size):
#         self.q = [None] * size
#         self.maxlen = size
#         self.p1 = 0
#         self.p2 = 0
#
#     def enQueue(self,val):
#         if self.q[self.p2] is None:
#             self.q[self.p2] = val
#             self.p2 = (self.p2 + 1) % self.maxlen
#             return True
#         else:
#             return False
#     def deQueue(self):
#         if self.q[self.p1] is None:
#             return False
#         else:
#             self.q[self.p1] = None
#             self.p1 = (self.p1 + 1) % self.maxlen
#             return True
#     def Front(self):
#         return -1 if self.q[self.p1] is None else self.q[self.p1]
#     def Rear(self):
#         return -1 if self.q[self.p2 -1] is None else self.q[self.p2 -1]
#
#     def is_Full(self):
#         return self.p1 == self.p2 and self.q[self.p2] is not None
#
#
# a = MyCircularQueue(5)
# print(a.enQueue(10))
# print(a.enQueue(20))
# print(a.enQueue(30))
# print(a.enQueue(40))
# print(a.Rear())
# print(a.is_Full())
# print(a.deQueue())
# print(a.deQueue())
# print(a.enQueue(50))
# print(a.enQueue(60))
# print(a.Rear())
# print(a.Front())

#========================================================================================
# class MyCircularQueue_classmate_solution:
#     def __init__(self, k: int):
#         self.num = k
#         self.front = None
#         self.end = None
#         self.len = 0
#
#     def enQueue(self, val: int) -> bool:
#         if self.len == self.num:
#             return False
#
#         if not self.front:
#             self.front = Node(val)
#             self.front.next = self.front
#             self.end = self.front
#             self.len += 1
#             return True
#
#         node = self.front
#         while node.next != self.end:
#             node = node.next
#
#         self.end = Node(val)
#         node.next.next = self.end
#         self.end.next = self.front
#         self.len += 1
#         return True
#
#     def deQueue(self) -> bool:
#         if self.len == 0:
#             return False
#
#         node = self.front.next
#         self.end.next = node
#         self.front = node
#         self.len -= 1
#         if self.len == 0:
#             self.front = None
#             self.end = None
#
#         return True
#
#     def Front(self) -> int:
#         if self.len == 0:
#             return -1
#         return self.front.val
#
#     def Rear(self) -> int:
#         if self.len == 0:
#             return -1
#         return self.end.val
#
#     def isEmpty(self) -> bool:
#         return self.len == 0
#
#     def is_Full(self) -> bool:
#         return self.len == self.num
#========================================================================================
# class Node:
#     def __init__(self,val,next = None):
#         self.val = val
#         self.next = next
# class Circular:
#     def __init__(self):
#         self.head = None
#
#     def push(self,val):
#         pt1 = Node(val)
#         temp = self.head
#         pt1.next = self.head
#
#         if self.head is not None:
#             while(temp.next != self.head):
#                 temp = temp.next
#             temp.next = pt1
#
#         else:
#             pt1.next = pt1
#
#         self.head = pt1
#
#
#     def printll(self):
#         temp = self.head
#         if self.head is not None:
#             while True:
#                 print(temp.val)
#                 temp = temp.next
#                 if (temp == self.head):
#                     break
#
# mylist = Circular()
# mylist.push(1)
# mylist.push(2)
# mylist.push(3)
# mylist.push(4)
# mylist.push(5)
# mylist.printll()
# print('finishsed')
