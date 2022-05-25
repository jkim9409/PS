# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Ex1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Ex2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

import heapq

def test_max_heapq(lst,k):

    return heapq.nlargest(k,lst)

nums1 = [3,2,1,5,6,4]
k1 = 2

nums2 = [3,2,3,1,2,4,5,5,6]
k2 = 4

# Add index [-1] for the actual answer
print(test_max_heapq(nums1,2)[-1])
print(test_max_heapq(nums2,4)[-1])


def findKthLargest_solution1(nums,k):
    heap = list()
    for n in nums:
        heapq.heappush(heap,-n)
    for _ in range(1,k):
        heapq.heappop(heap)
    return -heapq.heappop(heap)

print(findKthLargest_solution1(nums1,2))
print(findKthLargest_solution1(nums2,4))

def findKthLargest_solution2(nums,k):
    heapq.heapify(nums)
    for _ in range(len(nums)-k):
        heapq.heappop(nums)
    return heapq.heappop(nums)

print(findKthLargest_solution2(nums1,2))
print(findKthLargest_solution2(nums2,4))



nums1 = [3,2,1,5,6,4]
nums2 = [3,2,3,1,2,4,5,5,6]
def findKthLargest_solution3(nums,k):
    return sorted(nums,reverse=True)[k-1]

print(findKthLargest_solution3(nums1,2))
print(findKthLargest_solution3(nums2,4))