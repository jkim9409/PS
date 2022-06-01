n,k = map(int,input().split())
given_input = [tuple(map(int,input().split())) for _ in range(k)]
lst = [0]*n
print(given_input)
print(n,k)
for move in given_input:
    for i in range(move[0]-1,move[1]):
        lst[i] += 1

print(max(lst))