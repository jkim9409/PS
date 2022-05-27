# 양의 정수를 원소로 갖는 길이가 N인 수열이 입력으로 주어졌을 때, 이 수열을 오름차순으로 정렬 했을 때 각각의 위치에 있던 원소가 어느 위치로 이동하는지 출력하는 코드를 작성해보세요.
#
# 입력 형식
# 첫째 줄에는 수열의 길이를 나타내는 양의 정수 N이 주어지고, 둘째 줄에는 N개의 양의 정수인 원소가 빈칸을 사이에 두고 주어집니다. 숫자가 중복되어 주어질 수 있습니다.
#
# 1 ≤ N ≤ 1,000
#
# 1 ≤ 수열의 원소 ≤ 1,000,000
#
# 출력 형식
# 이 수열을 정렬했을 때 각각의 위치에 있던 원소가 어느 위치로 이동하는지를 공백을 사이에 두고 출력하는 코드를 작성해보세요. 동일한 원소의 경우, 먼저 입력으로 주어진 원소가 더 앞으로 와야 합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 7
# 3 1 6 2 7 30 1
# 출력:
#
# 4 1 5 3 6 7 2
# 예제 설명
# 입력으로 주어진 수열을 정렬하면 1 1 2 3 6 7 30 이 됩니다.
#
# 첫 번째 원소인 3은 네 번째 위치로, 두 번째 원소인 1은 첫 번째 위치로, .. 이동해야 하므로 답은 4 1 5 3 6 7 2 가 됩니다.
#
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB

# 내 답
n = int(input())
arr = list(map(int,input().split()))

newarr = [(n,i) for i,n in enumerate(arr,start=1)]
newarr.sort()
second_arr = [(j,n,i) for j,(n,i) in enumerate(newarr,start =1)]
second_arr.sort(key = lambda x: x[2])
for j,_,_ in second_arr:
    print(j,end=' ')


# 코드트리 정답
# 클래스 선언
class Number:
    def __init__(self, number, index):
        self.number, self.index = number, index


# 변수 선언 및 입력
n = int(input())
given_inputs = list(map(int, input().split()))
numbers = [
    Number(num, i)
    for i, num in enumerate(given_inputs)
]
answer = [
    0 for _ in range(n)
]

# Custom Comparator를 활용한 정렬
numbers.sort(key = lambda x: (x.number, x.index))

# 정렬된 숫자들의 원래 인덱스를 활용한 정답 배열 저장
for i, number in enumerate(numbers):
    answer[number.index] = i + 1 # 인덱스 보정

# 출력
for i in range(n):
    print(answer[i], end = ' ')