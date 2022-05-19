# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.
#
# Ex1:
# input: s = "abcabcbb"
# output: 3
#
# Ex2:
# input: s = "bbbbb"
# output: 1

#
# my solution
import collections
s = "abcabcbb"
maxlen = 0
for i, char in enumerate(s):
    p = 0
    temp = collections.defaultdict(int)
    d = i
    while char not in temp:
        temp[char] +=1
        p += 1
        d += 1
        if d == len(s):
            break
        char = s[d]
    maxlen = max(maxlen,p)

print(maxlen)


#textbook solution using two pointers

# def lengthOfLongestSubstring(s):
#     used = {}
#     max_length = start = 0
#     for index, char in enumerate(s):
#         if char in used and start <=used[char]:
#             start = used[char] + 1
#         else:
#             max_length = max(max_length,index-start+1)
#
#         used[char] = index
#     return max_length
#
# s1 = "abcabcbb"
# s2 = "bbbbb"
#
# print(lengthOfLongestSubstring(s1))
# print(lengthOfLongestSubstring(s2))
