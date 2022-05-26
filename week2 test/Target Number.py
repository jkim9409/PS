# https://programmers.co.kr/learn/courses/30/lessons/43165


numbers1 = [1, 1, 1, 1, 1]
target1 = 3
numbers2 = [4, 1, 2, 1]
target2 = 4



def solution(numbers,target):
    answer = 0
    n = len(numbers)
    def recursive(index,_sum):
        nonlocal answer
        if index == n:
            if _sum == target:
                answer += 1
            return

        recursive(index+1,_sum+numbers[index])
        recursive(index+1,_sum-numbers[index])


    recursive(0,0)
    return answer

print(solution(numbers1,target1))
print(solution(numbers2,target2))