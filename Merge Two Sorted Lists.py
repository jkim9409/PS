# https://leetcode.com/problems/merge-two-sorted-lists/
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4
#
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
#
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

from typing import Optional

import self as self


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

def mergeTwoLists(ll1,ll2):
    list = []
    node1 = ll1.head
    node2 = ll2.head
    while node1 or node2:
        if node1 is None:
            while node2:
                list.append(node2.val)
                node2 = node2.next
        elif node2 is None:
            while node1:
                list.append(node1.val)
                node1 = node1.next
        elif node1.val < node2.val:
            list.append(node1.val)
            node1 = node1.next
        else:
            list.append(node2.val)
            node2 = node2.next

    print(list)







lst1 = [1,2,4]
ll1 = LinkedList()
for e in lst1:
    ll1.append(e)
lst2 = [1,3,4]
ll2 = LinkedList()
for e in lst2:
    ll2.append(e)
mergeTwoLists(ll1,ll2)
