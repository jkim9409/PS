# https://leetcode.com/problems/largest-number/
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
#
# Since the result may be very large, so you need to return a string instead of an integer.
#
# Ex1:
# Input: nums = [10,2]
# Output: "210"
#
# Ex2:
# Input: nums = [3,30,34,5,9]
# Output: "9534330"

def to_swap(n1,n2):
    return str(n1)+ str(n2) < str(n2) + str(n1)

def largestNumber_insertion_sort(nums):
    i = 1
    while i < len(nums):
        j = i
        while j > 0 and to_swap(nums[j-1],nums[j]):
            nums[j], nums[j-1] = nums[j-1],nums[j]
            j -= 1
        i += 1
    return str(int(''.join(map(str,nums))))

nums1 = [10,2]
nums2 = [3,30,34,5,9]

print(largestNumber_insertion_sort(nums1))
print(largestNumber_insertion_sort(nums2))



# def wrong_solution(nums):
#     ans = ''
#     lst = []
#     for i, el in enumerate(nums):
#         if el < 10:
#             lst.append([el*11,i])
#         else:
#             lst.append([el,i])
#
#     for i in sorted(lst,reverse= True):
#         ans += str(nums[i[1]])
#
#     return ans
#
# nums = [3,30,34,5,9]
# wrong_solution(nums)