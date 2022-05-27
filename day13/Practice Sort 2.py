n = int(input())
given_input = list(map(int, input().split()))
numbers = [(el, i) for i, el in enumerate(given_input)]
answer = [-1] * len(given_input)

numbers.sort(key=lambda x: (x[0], x[1]))

for i, number in enumerate(numbers):
    answer[number[1]] = i + 1

for el in answer:
    print(el,end=' ')