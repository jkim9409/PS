
# input:
# M = 5
# [8,3,7,9,2]
# N = 3
# [5,7,9]

# output:
# No,Yes,Yes

def binary_search(nums,target):

    def bs(start,end):
        if start > end:
            return -1

        mid = (start + end) //2

        if nums[mid] < target:
            return bs(mid + 1, end)
        elif nums[mis] > target:
            return bs(start,mid -1)
        else:
            return mid
    return bs(0,len(nums)-1)


n = int(input())
arr = list(map(int,input().split()))

