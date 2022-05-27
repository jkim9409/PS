# https://www.acmicpc.net/problem/10814


n = int(input())
given_input = [input().split() for _ in range(n)]
arr = [(int(age),name,i) for i,(age,name) in enumerate(given_input)]
arr.sort(key=lambda x: (x[0],x[2]))

for age,name,_ in arr:
         print(age,name)