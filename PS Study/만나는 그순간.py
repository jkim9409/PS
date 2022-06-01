N, K, P, T = map(int, input().split())
txy = [tuple(map(int, input().split())) for _ in range(T)]
# 전염은 K 번째 까지의 악수만 적용
# P 번째 개발자가 전염되어있음
# N명의 개발자의 상태 리스트 K 번 전염을 시킬수 있다고 한다.

numbersleft = {}
for i in range(N + 1):
    numbersleft[i] = 0

status = [0] * (N + 1)

numbersleft[P] = K
status[P] = 1
shakehands = sorted(txy, key=lambda x: x[0])
for _, x, y in shakehands:
    if numbersleft[x] != 0 and numbersleft[y] != 0:
        numbersleft[x] = numbersleft[y] = K
        continue
    if numbersleft[x] != 0 and numbersleft[y] == 0:
        numbersleft[x] -= 1
        numbersleft[y] = K
        status[y] = 1
        continue
    if numbersleft[y] != 0 and numbersleft[x] == 0:
        numbersleft[y] -= 1
        numbersleft[x] = K
        status[x] = 1
        continue

status = status[1::]
ans = ''.join([str(i) for i in status])
print(ans)