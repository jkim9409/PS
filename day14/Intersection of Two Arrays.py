# https://leetcode.com/problems/intersection-of-two-arrays/
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
#
# Ex1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#
# Ex2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
import bisect

firstnums1 = [1,2,2,1]
firstnums2 = [2,2]

secondnums1 = [4,9,5]
secondnums2 = [9,4,9,8,4]

# def intersec_array(nums1,nums2):
#     if not nums1 or not nums2:
#         return []
#
#     result = set()
#     nums2.sort()
#     for n1 in nums1:
#         idx = bisect.bisect_left(nums2,n1)
#         if len(nums2) > idx and n1 == nums2[idx]:
#             result.add(n1)
#
#     return list(result)
#
# print(intersec_array(firstnums1,firstnums2))
# print(intersec_array(secondnums1,secondnums2))


# def intersection(nums1,nums2):
#     result = set()
#     for n1 in nums1:
#         for n2 in nums2:
#             if n1 ==n2:
#                 result.add(n1)
#     return list(result)
#
# print(intersection(firstnums1,firstnums2))
# print(intersection(secondnums1,secondnums2))


#투포인터
# def intersection2(nums1,nums2):
#     result = set()
#     nums1.sort()
#     nums2.sort()
#     i = j = 0
#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] > nums2[j]:
#             j +=1
#         elif nums1[i] < nums2[j]:
#             i +=1
#         else:
#             result.add(nums1[i])
#             i +=1
#             j +=1
#
#     return list(result)
#
#
# print(intersection2(firstnums1,firstnums2))
# print(intersection2(secondnums1,secondnums2))


