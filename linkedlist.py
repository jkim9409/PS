class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        if not self.head:
            self.head = Node(val,None)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(val,None)

    def printll(self):

        node = self.head
        while node:
            print(node.val)
            node = node.next

a = LinkedList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.printll()

class Stack:
    def __init__(self):
        self.top = None
    def push(self,val):
        self.top = Node(val,self.top)
    def pop(self):
        if not self.top:
            return None
        node = self.top
        self.top = self.top.next
        return node.val

a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)


print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
# ---------------------------------------------------------------------------------------------------
#
# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def push(self,val):
#         if not self.head:
#             self.head = Node(val)
#             return
#         node = self.head
#         while node.next:
#             node = node.next
#         node.next = Node(val)
#
#     def pop_first(self):
#         if not self.head:
#             return None
#         node = self.head
#         self.head = self.head.next
#         return node.val
#
#     def pop_last(self):
#         if not self.head:
#             return None
#         prev = None
#         node = self.head
#         while node.next:
#             prev = node
#             node = node.next
#         prev.next = None
#         return node.val
#
#
#
#     def printll(self):
#         if not self.head:
#             print("list is empty")
#             return None
#
#         node = self.head
#         while node:
#             print(node.val,end=' ')
#             node = node.next
#         print()
#     def reverse(self):
#         if not self.head:
#             return None
#         if self.head.next is None:
#             return
#         node = self.head
#         prev = None
#         while node:
#             next = node.next
#             node.next = prev
#             prev = node
#             node = next
#         self.head = prev
#
# a = LinkedList()
# a.push(1)
# a.push(2)
# a.push(3)
# a.push(4)
# a.push(5)
# a.printll()
# # print(a.pop_last())
# # print(a.pop_first())
# a.reverse()
# a.printll()
