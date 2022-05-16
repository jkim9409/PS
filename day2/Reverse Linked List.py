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
from typing import Optional


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


# def reverseList(l1):
#     list = []
#     node = l1.head
#     if node is None:
#         return []
#     while node:
#         list.append(node.val)
#         node = node.next
#     list.reverse() # memorize
#     answer = LinkedList()
#     print(list)
#     for i in list:
#         answer.append(i)
#
#     answer.printll()
#     return answer.head
#
# l1 = [1,2,3,4,5]
# ll1 = LinkedList()
# for e in l1:
#     ll1.append(e)
# l2 = [1,2]
# ll2 = LinkedList()
# for e in l2:
#     ll2.append(e)
# l3 = []
# ll3 = LinkedList()
# for e in l3:
#     ll3.append(e)
#
# reverseList(ll1)
# reverseList(ll2)
# reverseList(ll3)



class Solution:

    #recursive method
    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            nest = node.next
            node.next = prev
            # next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)


    #iterative method
    #https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e3147700-0829-4492-85ad-c7eec33859d0/%EC%97%AD%EC%88%9C_%EC%97%B0%EA%B2%B0_%EB%A6%AC%EC%8A%A4%ED%8A%B8_%28%EA%B3%BC%EC%A0%9C%ED%86%A1%29.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220514T110433Z&X-Amz-Expires=86400&X-Amz-Signature=4152aa163f79a4ee1e0f9f315a2b846a70367c31dea30849f45a74e2143dd13b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22%25EC%2597%25AD%25EC%2588%259C%2520%25EC%2597%25B0%25EA%25B2%25B0%2520%25EB%25A6%25AC%25EC%258A%25A4%25ED%258A%25B8%2520%28%25EA%25B3%25BC%25EC%25A0%259C%25ED%2586%25A1%29.pdf%22&x-id=GetObject
    def reverseList_iterative(self, head: Optional[ListNode]) -> ListNode:

        node = head
        prev = None
        # node, prev = head, None

        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next

            # next, node.next = node.next, prev
            # prev, node = node, next

        return prev


l1 = [1,2,3,4,5,7,8,4]
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

ans = Solution().reverseList_iterative(ll1.head)

node = ans
while node:
    print(node.val)
    node = node.next
