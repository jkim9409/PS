# https://www.acmicpc.net/problem/9663
# input: n = 8
# output: 92

def nqueen(n):

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
            count +=1
            return

        for col in range(n):
            visited[row] = col
            if is_ok(row):
                dfs(row+1)
    dfs(0)
    return count
print(nqueen(8))