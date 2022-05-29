# https://leetcode.com/problems/search-in-rotated-sorted-array/
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Ex1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
# Ex2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#
# Ex3:
# Input: nums = [1], target = 0
# Output: -1

nums1 = [4,5,6,7,0,1,2]
nums2 = [4,5,6,7,0,1,2]
nums3 = [1]

# def bs_rotated(nums,target):
#     def bs(lst, start, end):
#         if start > end:
#             return -1
#
#         mid = (start + end) // 2
#         if lst[mid] < target:
#             return bs(lst, mid + 1, end)
#         elif lst[mid] > target:
#             return bs(lst, start, mid -1)
#         else:
#             return mid
#
#     if not nums:
#         return -1
#
#     left = 0
#     right = len(nums) - 1
#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] > nums[right]:
#             left = mid + 1
#         else:
#             right = mid
#
#     added = nums + nums[:left]
#
#     result = bs(added, left, len(added) - 1)
#     return result if result == -1 else result % len(nums)
#
# print(bs_rotated(nums1,0))
# print(bs_rotated(nums2,3))
# print(bs_rotated(nums3,0))
#
#
# def search(nums,target):
#     if not nums:
#         return -1
#
#     left, right = 0, len(nums) -1
#     while left < right:
#         mid = left + (right - left) // 2
#
#         if nums[mid] > nums[right]:
#             left = mid + 1
#         else:
#             right = mid
#
#     pivot = left
#
#     #피봇을 기준으로 이진탐색
#
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         mid = left + (right - left) // 2
#         mid_pivot = (mid + pivot) % len(nums)
#
#         if nums[mid_pivot] < target:
#             left = mid + 1
#         elif nums[mid_pivot] > target:
#             right = mid - 1
#         else:
#             return mid_pivot
#
#     return -1
#
#
# print(search(nums1,0))
# print(search(nums2,3))
# print(search(nums3,0))