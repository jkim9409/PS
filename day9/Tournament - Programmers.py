# https://programmers.co.kr/learn/courses/30/lessons/12985
# Ex1:
# Input: N = 8, A= 4, B= 7
# Output: 3
#
# For N number of people. In what Round will A match with B


#
# def solution(n,a,b):
#     answer = 0
#     a = a-1
#     b = b-1
#     while a != b:
#         answer +=1
#         a= a//2
#         b= b//2
#     return answer
#
# print(solution(8,4,7))

import math
def solution_creative(n,a,b):
    if a > b:  # a,b를 순서대로 정렬 -> pivot 기준으로 값을 비교하기 위해서
        a,b = b,a

    while n >= 2: # 가장 밑단의 리프 노드 수 a,b 두 사람이 라운드를 진행하기 때문에 2 이상이여야한다.
        pivot = (1+n) / 2 # 중심선 설정

        if a < pivot < b: #pivot이 a 와 b 사이에 있는 경우
            return math.log(n)
        else: # a,b 모두 pivot 앞으로
            if a > pivot and b > pivot: #a,b 모두 pivot 보다 뒤에 있는 경우
                a,b = a - int(pivot), b-int(pivot) # pivot의 앞으로 대칭 이동 시켜준다.

            n = n/2 #반으로 줄이기기
