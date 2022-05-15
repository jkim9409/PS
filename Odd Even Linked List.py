# https://leetcode.com/problems/odd-even-linked-list/
# Example 1:
# input: head = [1,2,3,4,5]
# output: [1,3,5,2,4]
#
# Example 2:
# input: head = [2,1,3,5,6,4,7]
# output: [2,3,6,7,1,5,4]

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

class ListNode:
    def __init__(self, val=0, next=None):
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

def oddEvenList(ll1):

    node = ll1.head
    list =[]
    while node:
        list.append(node.val)
        node = node.next

    listodd = list[::2]
    listeven = list[1:len(list):2]
    newlist = listodd + listeven

    print(newlist)


l1 = [1,2,3,4,5]
ll1 = LinkedList()
for e in l1:
    ll1.append(e)

l2 = [2,1,3,5,6,4,7]
ll2 = LinkedList()
for e in l2:
    ll2.append(e)

oddEvenList(ll1)
oddEvenList(ll2)