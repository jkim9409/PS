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
