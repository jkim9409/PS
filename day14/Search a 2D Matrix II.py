# https://leetcode.com/problems/search-a-2d-matrix-ii/
#
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
#
# Ex1:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
#
# Ex2:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false

# 각 row을 기준으로 하는 이진검색은 괜찮지만 행을 기준으로 하는 이진검색은 쉽지않다. 특정 인덱스를 기준으로 값을 추천해오는것이 많은 연산을 필요로 한다.

matrix1 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

matrix2 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]


# def serachMatrix1(mat,target):
#
#     if not mat:
#         return False
#
#     row = 0
#     col = len(mat[0]) -1
#
#     while row <= len(mat) - 1 and col >= 0:
#         if target == mat[row][col]:
#             return True
#         elif target < mat[row][col]:
#             col -= 1
#         elif target > mat[row][col]:
#             row += 1
#     return False
#
# print(serachMatrix1(matrix1,5))
# print(serachMatrix1(matrix2,20))

# 파이썬 다운 방식
def searchMatrix2(mat,target):
    return any(target in row for row in mat)
print(searchMatrix2(matrix1,5))
print(searchMatrix2(matrix2,20))
