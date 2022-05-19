from collections import deque

def printqueue(m,p):
    q = deque(p)
    count = 0
    while q:
        if m == 0:
            if q[0] == max(q):
                count += 1
                return count
            else:
                q.append(q.popleft())
                m = len(q)-1
        target = q.popleft()
        if target >= max(q):
            count += 1
            m -= 1
        else:
            m -= 1
            q.append(target)

print(printqueue(4,[2, 1, 3, 5, 1, 9, 2]))