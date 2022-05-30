






# import bisect
# n,m = map(int,input().split())
# nums = [int(input()) for _ in range(n)]
# router = m - 2
# nums.sort()
# routersetted = [nums[0],nums[-1]]
#
# while router > 0:
#     currenthigh = 0
#     for el in nums:
#         idx = bisect.bisect_left(routersetted, el)
#         compval = min(routersetted[idx]-el,el-routersetted[idx-1])
#         if compval > currenthigh:
#             currenthigh = compval
#             eltoadd = el
#     bisect.insort_left(routersetted,eltoadd)
#     router -= 1
# print(len(routersetted))