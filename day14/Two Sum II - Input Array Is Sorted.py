# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
#
# Your solution must use only constant extra space.
#
# Ex1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
#
# Ex2:
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
#
# Ex3:
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
import bisect

nums1 = [2,7,11,15]
nums2 = [2,3,4]
nums3 = [-1,0]

# Two Pointer
# def twoSum1(nums,target):
#     left,right = 0, len(nums) -1
#     while not left == right:
#         if nums[left] + nums[right] < target:
#             left +=1
#         elif nums[left] + nums[right] > target:
#             right -=1
#         else:
#             return [left +1, right +1]
#
# print(twoSum1(nums1,9))
# print(twoSum1(nums2,6))
# print(twoSum1(nums3,-1))

# #binary search
# def twoSum2(nums,target):
#     for k, v in enumerate(nums):
#         left, right = k + 1, len(nums) - 1
#         expected = target - v
#
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] < expected:
#                 left = mid + 1
#             elif nums[mid] > expected:
#                 right = mid - 1
#             else:
#                 return [k + 1, mid + 1]
#
#
# print(twoSum2(nums1,9))
# print(twoSum2(nums2,6))
# print(twoSum2(nums3,-1))


#bisect module

# def twoSum3(nums,target):
#     for k, v in enumerate(nums):
#         expected = target - v
#         i = bisect.bisect_left(nums[k+1:], expected)
#         if i < len(nums[k+1:]) and nums[i + k + 1] == expected:
#             return [k + 1, i + k + 2]
#
#
#
# print(twoSum3(nums1,9))
# print(twoSum3(nums2,6))
# print(twoSum3(nums3,-1))


# 슬라이싱을 최소화 해주어 소도를 개선한 방법
# def twoSum4(nums,target):
#     for k,v in enumerate(nums):
#         expected = target - v
#         i = bisect.bisect_left(nums, expected, k+1)
#         if i < len(nums) and nums[i] == expected:
#             return [k+1,i+1]
#
# print(twoSum4(nums1,9))
# print(twoSum4(nums2,6))
# print(twoSum4(nums3,-1))
