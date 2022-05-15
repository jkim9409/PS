# a = [1,2,3,4,5,6,7,8,9,10]
# b = a[::-1]
# c = reversed(a)
# d = a.reverse()
# print(a)
# print(b)
# print(c)
# print(d)


#
# #pop()
# a = [1,2,3,4,5,6,7,8,9,10]
# b = a.pop()
# c = a.pop(2) # correspond to the index
# print(a)
# print(b)
# print(c)

# pass
# continue
# break
# dictionary, set ,tuple
# sorting algorithm
# sorted function key usage








# import string
# from pprint import pprint
# text = 'hello this is sparta'
# counter = {}
#
# # counting letter
# for char in text:
#     if not char.isalpha():
#         continue
#     if char in counter:
#         counter[char] += 1
#     else:
#         counter[char] = 1
# pprint(counter)
#
# #find index of each alphabet in a word
#
# def get_index_naive(word):
#     result = [-1] * len(string.ascii_lowercase)
#     for i in range(len(word)):
#         char = word[i]
#         for j in range(len(string.ascii_lowercase)):
#             lo = string.ascii_lowercase[j]
#             if result[j] == -1 and char ==lo:
#                 result[j] = i
#     print(' '.join([str(num) for num in result]))
#
# def get_index(word):
#     result = [-1] * len(string.ascii_lowercase)
#     for i in range(len(word)):
#         index = ord(word[i]) - 97
#         if result[index] == -1:
#             result[index] = i
#
#     print(' '.join([str(num) for num in result]))
#
# get_index_naive('baekjoon')
# get_index('baekjoon')




## create ListNode and LinkedList by myself
# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val = val
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self,val):
#         if not self.head:
#             self.head = ListNode(val,None)
#             return
#         node = self.head
#         while node.next:
#             node = node.next
#         node.next = ListNode(val,None)
#
#
#     def printll(self):
#         node = self.head
#         while node:
#             print(node.val)
#             node = node.next
#
# list = [1,2,3,4,5,6,7,8,9,10]
# ll = LinkedList()
# for i in list:
#     ll.append(i)
# ll.printll()

