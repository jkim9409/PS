# https://www.acmicpc.net/problem/17218

def creatingpassword(s1,s2):
    return [char for char in s1 if char in s2]

s1 = 'AUTABBEHNSA'
s2 = 'BCUAMEFKAJNA'

print(creatingpassword(s1,s2))