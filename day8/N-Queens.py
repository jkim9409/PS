# https://leetcode.com/problems/n-queens/

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
#
# Ex1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#
# Ex2:
# Input: n = 1
# Output: [["Q"]]

def nqueen(n):
    answer = []
    count = 0
    visited = [-1]*n

    def is_ok(nthrow):
        for row in range(nthrow):
            if visited[nthrow] == visited[row] or (nthrow-row) == abs(visited[nthrow]-visited[row]):
                return False
        return True


    def dfs(row):
        if row == n:
            nonlocal count
            count += 1
            grid = [['.'] * n for _ in range(n)]
            for r,c in enumerate(visited):
                grid[r][c] = 'Q'

            result = []
            for line in grid:
                print(line)
                result.append(''.join(line))
            answer.append(result)
            return

        for col in range(n):
            visited[row] = col
            if is_ok(row):
                dfs(row+1)

    dfs(0)
    return answer

nqueen(4)