class Node:
    def __init__(self,var,next):
        self.var = var
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,vartoadd):
        if self.head is None:
            self.head = Node(vartoadd,None)
            return

        startnode = self.head
        while startnode.next:
            startnode = startnode.next

        startnode.next = Node(vartoadd,None)

    def printll(self):
        node = self.head
        while node:
            print(node.var)
            node = node.next
    def deletekey(self,keyval):

        temp = self.head
        if temp is not None:
            if temp.var == keyval:
                self.head = temp.next

                return

        while temp:
            if temp.var == keyval:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next




lst = [1,2,3]
l1 = LinkedList()
for e in lst:
    l1.append(e)
l1.printll()
l1.deletekey(2)
l1.printll()