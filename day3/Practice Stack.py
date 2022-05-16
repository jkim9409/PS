class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self,val):
        # if not self.top: #this whole part of the code is not necessary
        #     self.top = Node(val,None)
        #     return
        self.top = Node(val,self.top)
    def pop(self):
        if not self.top:
            return None

        node = self.top
        self.top = self.top.next
        return node.val

def test_node():
    assert Node(1,None).val == 1


def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)

    assert stack.pop() == 7
    assert stack.pop() == 6
    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    assert stack.is_empty()

test_node()
test_stack()
#-------------------------------------------------
#https://www.acmicpc.net/problem/10773

# stack = [1, 3, 5, 4, 0, 0, 7, 0, 0, 6]
# stack = [3, 0, 4, 0]
# ans = []
# count = 0
# while stack:
#     num = stack.pop()
#     if num != 0 and count == 0:
#         ans.append(num)
#     else:
#         if num == 0:
#             count += 1
#         else:
#             count -= 1
#
# print(ans)
#------------------------------------------------

s = '((()()()))'
pair = {
    '(':')'
}

stack = []
flag = 0
for char in s:
    if char == '(':
        stack.append(char)
    else:
        if not stack or pair[stack.pop()] != char:
            print('No')
            flag += 1

if flag == 0:
    print('Yes')








