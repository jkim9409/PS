m = 6
nums = [19, 15, 10, 17]


def solution(nums,m):

    start = 0
    end = max(nums)

    result = 0

    while(start <= end):
        total = 0
        mid = (start+end)//2
        for x in nums:
            if x > mid:
                total += x-mid
        if total < m:
            end = mid -1
        else:
            result = mid
            start = mid + 1
    return result

print(solution(nums,m))
