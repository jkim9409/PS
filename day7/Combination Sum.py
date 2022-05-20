# https://leetcode.com/problems/combination-sum/
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
#
# Ex1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
#
# Ex2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]


from collections import deque

# def combinationSum(candidates,target):
#     result = []
#
#     def dfs(csum, index, path):
#
#         if csum < 0:
#             return
#         if csum == 0:
#             result.append(path)
#             return
#
#         for i in range(index, len(candidates)):
#             dfs(csum - candidates[i],i,path+[candidates[i]])
#
#     dfs(target, 0, [])
#     return result

# def combinationSum(candidates):
#     result = []
#     def dfs(index, path):
#         if len(path) == len(candidates):
#             if path not in result:
#                 result.append(path)
#             return
#         for i in range(0, len(candidates)):
#             if path not in result:
#                 result.append(path)
#             dfs(i, path + [candidates[i]])
#     dfs(0, [])
#     return result

# def combinationSum(candidates):
#     result = []
#     def dfs(path):
#         if len(path) == len(candidates):
#             if path not in result:
#                 result.append(path)
#             return
#         for i in range(0, len(candidates)):
#             if path not in result:
#                 result.append(path)
#             dfs(path + [candidates[i]])
#     dfs([])
#     return result
#
#
# candidates = [2,3,6,7]
# target = 7
# print(combinationSum(candidates))
# print(len(combinationSum(candidates)))
# print(4+4*4+4*4*4+4*4*4*4)

a = [1,2,3]
b = [4]
print(a+b)