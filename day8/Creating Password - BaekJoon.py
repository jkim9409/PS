# https://www.acmicpc.net/problem/1759


def createpw(n: int,s: str) -> list:
    result = []

    def aeiou(path):
        for el in ['a','e','i','o','u']:
            if el in path:
                return True
        return False

    def dfs(path):

        if len(path) > 1 and path[-1] <= path[-2]:
            return

        if len(path) == n and aeiou(path):
            result.append(''.join(path))
            return

        for char in s:
            dfs(path + [char])

    dfs([])
    return result

n = 4
s = 'atcisw'
print(createpw(n,s))

