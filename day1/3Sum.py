# Example1:
# input: nums = [-1,0,1,2,-1,-4]
# output: [[-1,-1,2],[-1,0,1]]
#
# Example2:
# input: nums = []
# output: []
#
# Example3:
# input: nums = [0]
# output: []

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.









def threeSum_badsolution(nums: [int]) -> [[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) -2):

        if i > 0 and nums[i] == nums[i -1]:
            continue
        for j in range(i +1, len(nums) -1 ):
            if j > i+1 and nums[j] == [j -1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j+1 and nums[k] == nums [k-1]:
                    continue
                if nums [i] + nums[j] + nums[k] == 0:
                    results.append([nums [i], nums[j], nums[k]])

    return results
# comment: this method works, but has a big O of n^3 so its likely to time out. Also note how "continue" was used to avoid duplication

def threeSum_bettersolution(nums:[int]) -> [[int]]:
    results = []
    nums.sort()

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]: #To avoid duplication, go to the next loop if you encounter the same number
            continue

        left, right = i+1, len(nums) - 1 # Create two pointers' indexes.notice that len(nums) -1 index will give you the last element in the list
        while left < right:  # if left = right, get out of the loop
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else: # if sum == 0,
                results.append([nums[i],nums[left],nums[right]])

                while left < right and nums[left] == nums[left + 1]: #avoid duplication
                    left += 1
                while left < right and nums[right] == nums[right -1]:
                    right -= 1

                left += 1
                right -= 1
    return results

#comment: need to know when to use "while" instead of "for"





input1 = [-1,0,1,2,-1,-4]
input2 = []
input3 = [0]

print(threeSum_badsolution(input1))
print(threeSum_badsolution(input2))
print(threeSum_badsolution(input3))

print(threeSum_bettersolution(input1))
print(threeSum_bettersolution(input2))
print(threeSum_bettersolution(input3))
