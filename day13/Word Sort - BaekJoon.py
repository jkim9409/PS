
# https://www.acmicpc.net/problem/1181

n = int(input())
given_input =[input() for _ in range(n)]
arr = [(el,len(el)) for el in given_input]
arr.sort(key = lambda x: (x[1],x[0]))
for i in range(len(arr)):
    if i ==0:
        print(arr[i][0])
        continue
    if arr[i] !=arr[i-1]:
        print(arr[i][0])