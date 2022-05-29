# https://www.codetree.ai/curriculums
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Ex1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
#
# Ex2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1


nums1 = [-1,0,3,5,9,12]
nums2 = [-1,0,3,5,9,12]

# def binary_search(nums,target):
#     def bs(start,end):
#         if start > end:
#             return -1
#
#         mid = (start + end) // 2
#
#         if nums[mid] > target:
#             return bs(mid+1,end)
#         elif nums[mid] > target:
#             return bs(start,mid-1)
#         else:
#             return mid
#
#     return bs(0,len(nums) -1)
#
# print(binary_search(nums1,9))
# print(binary_search(nums2,2))




# import bisect
# def binary_search_builtin(nums,target):
#     idx = bisect.bisect_left(nums,target)
#
#     if idx < len(nums) and nums[idx] == target:
#         return idx
#     else:
#         return -1
#
# print(binary_search_builtin(nums1,9))
# print(binary_search_builtin(nums2,2))

# def seach(nums, target):
#     left, right = 0, len(nums) -1
#     while left <= right:
#         mid = (left + right) // 2
#
#         if nums[mid] < target:
#             left = mid + 1
#         elif nums[mid] > target:
#             right = mid - 1
#         else:
#             return mid
#     return -1
#
# print(seach(nums1,9))
# print(seach(nums2,2))


# def search2(nums,target):
#     try:
#         return nums.index(target)
#     except ValueError:
#         return -1
#
# print(search2(nums1,9))
# print(search2(nums2,2))