from collections import defaultdict

class Node:
    def __init__(self,key = None,val = None):
        self.key = key
        self.val = val
        self.next = None

class HashMap:
    def __init__(self):
        self.size = 1000
        self.table = defaultdict(Node)

    def put(self,key,val):
        index = key % self.size
        p = self.table[index]
        if p.val is None:
            p.val = val
            p.key = key
            return

        while p:
            if p.key == key:
                p.val = val
                return
            if p.next is None:
                break
            p = p.next
        p.next = Node(key,val)

    def get(self,key):
        index = key % self.size
        p = self.table[index]
        if not p.val:
            return -1
        while p:
            if p.key == key:
                return p.val
            p = p.next
        return -1

    def remove(self,key):
        index = key % self.size
        p = self.table[index]
        if not p.val:
            return -1

        if p.key == key:
            if p.next is None:
                self.table[index] = Node()
                return
            else:
                self.table[index] = p.next
                return
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return -1
            prev = p
            p = p.next

        return -1

a = HashMap()
print(a.put(1,1))
print(a.put(2,2))
print(a.get(1))
print(a.get(3))
print(a.put(2,1))
print(a.get(2))
print(a.remove(2))
print(a.get(2))



