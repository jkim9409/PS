# Example 1:
# input: head = [1,2,3,4,5]
# output: [5,4,3,2,1]
#
# Example 2:
# input: head = [1,2]
# output: [2,1]
#
# Example3:
# input: head = []
# output: []
#
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
#










class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        if not self.head:
            self.head = ListNode(val,None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val,None)

    def printll(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next


def reverseList(l1):
    list = []
    node = l1.head
    if node is None:
        return []
    while node:
        list.append(node.val)
        node = node.next
    list.reverse() # memorize
    answer = LinkedList()
    print(list)
    for i in list:
        answer.append(i)

    answer.printll()
    return answer.head

l1 = [1,2,3,4,5]
ll1 = LinkedList()
for e in l1:
    ll1.append(e)
l2 = [1,2]
ll2 = LinkedList()
for e in l2:
    ll2.append(e)
l3 = []
ll3 = LinkedList()
for e in l3:
    ll3.append(e)

reverseList(ll1)
reverseList(ll2)
reverseList(ll3)