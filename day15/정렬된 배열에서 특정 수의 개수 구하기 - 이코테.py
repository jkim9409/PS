import bisect

nums1 = [1,1,2,2,2,2,3]
target1 = 2

nums2 = [1,1,2,2,2,2,3]
target2 = 4

def count_number_solution(lst,target):
    left_idx = bisect.bisect_left(lst,target)
    if not (0 <= left_idx < len(lst) and lst [left_idx] == target):
        return -1

    right_idx = bisect.bisect_right(lst,target)
    return right_idx - left_idx


print(count_number_solution(nums1,target1))
print(count_number_solution(nums2,target2))










# n,target = map(int,input().split())
# nums = list(map(int,input().split()))
#
# def solution(nums,target):
#     start = bisect.bisect_left(nums, target)
#     end = bisect.bisect_right(nums, target)
#     if start-end == 0:
#         return -1
#     else:
#         return end - start
#
# print(solution(nums,target))