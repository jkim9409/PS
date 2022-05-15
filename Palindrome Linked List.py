# https://leetcode.com/problems/palindrome-linked-list/
#
# Given the head of a singly linked list, return true if it is a palindrome.
#
# Example 1:
# input: head = [1,2,2,1]
# output: true
#
# Example 2:
# input: head = [1,2]
# output: false


#First,make a class that turns lists into a linked List.
class ListNode:
    def __init__(self,val,next):
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

# check if this class works fine
# l1 = [1,2,3,4,5,6]
# ll1 = LinkedList()
# for e in l1:
#     ll1.append(e)
# ll1.printll()

#comment: my own solution.
def isPalindrome_mysolution(head:[int]) -> bool:
    if not head:
        return True

    linkedlist = LinkedList()


    for e in head:
        linkedlist.append(e)

    simplelist = []

    node = linkedlist.head
    while node:
        simplelist.append(node.val)
        node = node.next

    left, right = 0,len(simplelist)-1

    while left < right:
        if simplelist[left] != simplelist[right]:
            return False
        left += 1
        right -=1
    return True

print(isPalindrome_mysolution([1,2,2,1]))
print(isPalindrome_mysolution([1,2]))
print(isPalindrome_mysolution([]))
from typing import Optional

class Solution:
    def isPalindromeleetcode(self, head: ListNode) -> bool:
        vals = []

        while head is not None:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]

    def isPalindromelecture(self,haed: ListNode): ->bool:
        arr = []

        if not head:
            return True

        node = head
        while node:
            arr.append(node.val)
            node = node.next

        while len(arr) > 1:
            if arr.pop(0) != arr.pop()
                return False

        return True


    def isPalindrome_mysolution(head: [int]) -> bool:
        if not head:
            return True

        linkedlist = LinkedList()

        for e in head:
            linkedlist.append(e)

        simplelist = []

        node = linkedlist.head
        while node:
            simplelist.append(node.val)
            node = node.next

        left, right = 0, len(simplelist) - 1

        while left < right:
            if simplelist[left] != simplelist[right]:
                return False
            left += 1
            right -= 1
        return True

l1 = [1,2,2,1]
ll1 = LinkedList()
for e in l1:
    ll1.append(e)

print(Solution().isPalindromeleetcode(ll1.head))




