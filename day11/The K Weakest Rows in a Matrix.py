# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
# A row i is weaker than a row j if one of the following is true:
# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
#
# Ex1:
# Input: mat =
#             [[1,1,0,0,0],
#              [1,1,1,1,0],
#              [1,0,0,0,0],
#              [1,1,0,0,0],
#              [1,1,1,1,1]],
#             k = 3
# Output: [2,0,3]
#
# Ex2:
# Input:
#         mat =
#             [[1,0,0,0],
#              [1,1,1,1],
#              [1,0,0,0],
#              [1,0,0,0]],
#             k = 2
# Output: [0,2]
import heapq


def kWeakestRows(mat,k):
    soldiers = []
    for i, row in enumerate(mat):
        soldiers.append((i,sum(row)))

    sorted_soldiers = sorted(soldiers,key = lambda x: x[1])

    ans = [index[0] for index in sorted_soldiers[:k]]

    return ans


mat1 = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k1 = 3

mat2 =[[1,0,0,0],
     [1,1,1,1],
     [1,0,0,0],
     [1,0,0,0]]
k2 = 2


print(kWeakestRows(mat1,k1))
print(kWeakestRows(mat2,k2))
