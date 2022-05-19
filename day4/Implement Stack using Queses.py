from collections import deque
class Mystack: # Inside stack, you need push(), pop(), top(), empty(),
    def __init__(self):
        self.q = deque()
    def push(self,val):
        self.q.append(val)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        if not self.q:
            return None
        return self.q.popleft()
    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


# a = Mystack()
# a.push(1)
# a.push(2)
# a.push(3)
# a.push(4)
# a.push(5)
# a.push(6)
#
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())


for _ in range(1):
    print(1)