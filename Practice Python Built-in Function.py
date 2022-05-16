# a = [1,2,3,4,5,6,7,8,9,10]
# b = a[::-1]
# c = reversed(a)
# d = a.reverse()
# print(a)
# print(b)
# print(c)
# print(d)
# ------------------------------------------------------------------------------------------


#
# #pop()
# a = [1,2,3,4,5,6,7,8,9,10]
# b = a.pop()
# c = a.pop(2) # correspond to the index
# print(a)
# print(b)
# print(c)

# ------------------------------------------------------------------------------------------

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
#import string
# def get_index_naive(word):
#
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

# ------------------------------------------------------------------------------------------



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

# ------------------------------------------------------------------------------------------


# print(~2)  # ~2 will turn all 0s to 1s and 1s to 0s in the binary scaled integer
# print(3 & 5) # will turn find all the common 1s if two nums were binary scared
# print(3 | 5) # will turn give 1s if any of the ditis have 1 nums were binary scared
# print(3 ^ 5) # will turn 1 for the digit if two nums have different value for the digie
# #3       : 00000000 00000000 00000000 00000011
# #5       : 00000000 00000000 00000000 00000101
# #3 ^ 5   : 00000000 00000000 00000000 00000110
# ------------------------------------------------------------------------------------------

# i = 0
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)
#
# i = 0
# while i < 10:
#     i += 1
#     if i % 5 == 0:
#         break
#     print(i)
#
# i = 0
# while i < 10:
#     i += 1
#     if i % 5 == 0:
#         pass
#     print(i)
# ------------------------------------------------------------------------------------------
# string = "my name is junho"
# print(string.find("junho"))
# print(string.find("hello")) #return -1 if none
# print(string.index("junho"))
# print(string.index("hello")) #return error if none.
# # for findall, you need general expression
# ------------------------------------------------------------------------------------------
# a =set('abcdcba')
# print(a)
# a.add('f')
# print(a)
# a.remove('c')
# print(a)
# # ------------------------------------------------------------------------------------------
#
#
# import collections
#
# word = "hello world"
# counter = collections.Counter(word) #you can use all the feature of dictionary
# print(counter)
# max_count = -1
# for letter in counter:
#     if counter[letter] > max_count:
#         max_count = counter[letter]
#         max_letter = letter
#
# print(max_letter,max_count)
# print(collections.Counter(word).most_common(3))
#
class Node:
    def __init__(self,val, next):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None


    def push(self,val):
        self.top = Node(val,self.top)

    def pop(self):
        if not self.top:
            return None

        node = self.top
        self.top = self.top.next
        return node.val