import bisect

n,target = map(int,input().split())
nums = list(map(int,input().split()))

def solution(nums,target):
    start = bisect.bisect_left(nums, target)
    end = bisect.bisect_right(nums, target)
    if start-end == 0:
        return -1
    else:
        return end - start

print(solution(nums,target))