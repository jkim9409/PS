# https://www.acmicpc.net/problem/2751


n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
for el in sorted(nums):
    print(el)