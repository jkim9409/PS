# https://www.acmicpc.net/problem/5052

nums1 = ['911','97625999','91125426'] # return No
nums2 = ['113','12340','123440','12345','98346'] # return Yes
nums3 = ['1332','1323','911','13200','132']
def solution(nums):
    newnums = sorted(nums)
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if len(newnums[i]) > len(newnums[j]):
                continue
            if newnums[i] == newnums[j][0:len(newnums[i])]:
                return False

    return True

print(solution(nums1))
print(solution(nums2))
print(solution(nums3))