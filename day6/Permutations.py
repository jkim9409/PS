# https://leetcode.com/problems/permutations/
# Given an array nums of distinct integers,
# return all the possible permutations. You can return the answer in any order.
#
# Ex1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Ex2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#
# Ex3:
# Input: nums = [1]
# Output: [[1]]

def permute(nums):
    results = []
    prev_element =[]
    def dfs(elements):

        #리프 노드일때 결과 추가
        if len(elements) == 0:
            results.append(prev_element[:])   # Must use [:] or .copy() !!!!!!!!!!!!!! otherwise prev_element value will keep changing

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_element.append(e)
            dfs(next_elements)
            prev_element.pop()

    dfs(nums)
    return results


# print(permute([1,2,3]))






import itertools

# def permute_pythonicway(nums):
#     return list(map(list, itertools.permutations(nums)))
#     # return list(itertools.permutations(nums)) #This will give result in tuple
# # map is used to make turn tuple into list.
# print(permute_pythonicway([1,2,3]))

