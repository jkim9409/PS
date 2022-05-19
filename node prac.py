class Node:
    def __init__(self,val,next =None):
        self.val = val
        self.next = next


class Circular:
    def __init__(self,size):
        self.start = Node(size)
        size -=1

        node = self.start
        while size > 0:
            node.next = Node(size)
            node = node.next
            size -=1
        node.next = self.start

a = Circular(5)
print(a)