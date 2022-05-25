# https://www.acmicpc.net/problem/9095


def onetwothree(n):
    result = []
    def dfs(path):
        x = sum(path)
        if x >= n:
            if x == n:
                result.append(path)
            return

        for i in range(1,4):
            dfs(path + [i])

    dfs([])
    return len(result)

print(onetwothree(10))