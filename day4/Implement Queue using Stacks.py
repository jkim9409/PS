class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self,x):
        self.input.append(x)
    def pop(self):
        self.peek()
        return self.output.pop()
    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
que = MyQueue()

que.push(1)
que.push(2)
que.push(3)
que.push(4)
que.push(5)

print(que.pop())
print(que.pop())

print(que.pop())
que.push(6)
que.push(7)
que.push(8)
que.push(9)
que.push(10)
print(que.pop())
print(que.pop())
print(que.pop())
print(que.pop())