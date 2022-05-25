# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters
#
# Ex1:
# Input: s = "abcabcbb"
# Output: 3
#
# Ex2:
# Input: s = "bbbbb"
# Output: 1
#
# Ex3:
# Input: s = "pwwkew"
# Output: 3


def longestsubstring(s):
    max_len = 0
    p1 = 0
    p2 = 1
    used = {s[p1]:p1}
    result = ''
    while p2 < len(s):
        if s[p2] in used and p1 <= used[s[p2]]:
            p1 = used[s[p2]] +1
            used[s[p2]] = p2

        else:
            used[s[p2]] = p2
            max_len = max(max_len,p2-p1+1)
            result = s[p1:p2+1]
        p2 +=1
    return max_len,result


print(longestsubstring('pwwabcdekewabc'))


# def longestsubstring_solution(s):
#     max_len = start = 0
#     used = {}
#     for i,char in enumerate(s):
#         if char in used and start <= used[char]:
#             start = used[char] + 1
#         else:
#             max_len = max(max_len, i-start+1)
#
#         used[char] = i
#
#     return max_len
#
# print(longestsubstring_solution("pwwabcdekewabc"))