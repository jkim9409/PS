# https://leetcode.com/problems/combinations/
# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
# You may return the answer in any order.
#
# Ex1:
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
# Ex2:
# Input: n = 1, k = 1
# Output: [[1]]


# def combine(n,k):
#     results = []
#
#     def dfs(elements, start, k):
#         if k == 0:
#             results.append(elements[:])
#             return
#
#         for i in range(start, n+1):
#             elements.append(i)
#             dfs(elements, i+1, k-1)
#             elements.pop()
#
#     dfs([],1,k)
#     return results
#
# print(combine(1,2))


#
#
# import itertools
#
# def combine_pythonic(n,k):
#     return list(itertools.combinations(range(1,n+1),k))
#
# print(combine_pythonic(4,2))