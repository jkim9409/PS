# https://leetcode.com/problems/subsets/
# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
#
# Ex1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# Ex2:
# Input: nums = [0]
# Output: [[],[0]]


def subset(nums):
    result = []
    def recursive(index,path):

        result.append(path)

        for i in range(index,len(nums)):
            recursive(i+1,path + [nums[i]])



    recursive(0,[])
    return result


nums = [1,2,3]
print(subset(nums))
