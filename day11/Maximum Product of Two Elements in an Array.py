# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
# Ex1:
# Input: nums = [3,4,5,2]
# Output: 12
# Ex2:
# Input: nums = [1,5,4,5]
# Output: 16
# Ex3:
# Input: nums = [3,7]
# Output: 12

import heapq
def maxProduct(nums):
    biggests = heapq.nlargest(2,nums)
    ans = (biggests[0]-1) * (biggests[1]-1)
    return ans

print(maxProduct([3,4,5,2]))
print(maxProduct([1,5,4,5]))
print(maxProduct([3,7]))