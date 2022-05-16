# https://leetcode.com/problems/daily-temperatures/
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.
# Ex1:
# input:temperatures = [73,74,75,71,69,72,76,73]
# output:[1,1,4,2,1,1,0,0]
#
# Ex2:
# input:temperatures = [30,40,50,60]
# output:[1,1,1,0]
#
# Ex3:
# input: temperatures = [30,60,90]
# output: [1,1,0]


def dailyTemperature_textbook(T):
    answer = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer

# def dailyTemperature_mysolution(T):
#     ans = [0] * len(T)
#     for i in range(len(T)):
#         for j in range(i+1,len(T)):
#             if T[i] < T[j]:
#                 ans[i] = j-i
#                 break
#     return ans



print(dailyTemperature_textbook([73,74,75,71,69,72,76,73]))
