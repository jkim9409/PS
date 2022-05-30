import bisect

n = int(input())
nums = list(map(int,input().split()))

def solution(nums):
    for i,el in enumerate(nums):
        if i == el:
            return el

    return -1

print(solution(nums))
