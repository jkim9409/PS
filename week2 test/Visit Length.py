# https://programmers.co.kr/learn/courses/30/lessons/49994



s1 = 'ULURRDLLU'
s2 = 'LULLLLLLU'

def solution(dirs):
    curx, cury = 0,0

    result = set()
    for char in dirs:
        if char == 'U' and cury < 5:
            result.add(((curx, cury), (curx, cury+1)))
            cury += 1
        elif char == 'D' and cury > -5:
            result.add(((curx, cury-1), (curx, cury)))
            cury -= 1
        elif char == 'R' and curx < 5:
            result.add(((curx, cury), (curx+1, cury)))
            curx += 1
        elif char == 'L' and curx > -5:
            result.add(((curx-1, cury), (curx, cury)))
            curx -= 1
    return len(result)

print(solution(s1))
print(solution(s2))