# n = 6
# times = 28
def solution(n,times):
    # 왼쪽은 최선의 경우(가장 짧게 걸리는 시간) 로 두고 오른쪽은 최악(가장 오래 걸리는 시간)의 경우로 둔다.
    left = min(times)
    right = max(times)*n
    # 이분탐색을 실행해 나가며 점점 왼쪽과 오른쪽의 범위를 좀혀간다.
    while left < right:
        mid = (left+right) // 2
        total = 0

        # 최대 몇명을 심사 할 수 있느지 게산해 주고
        for t in times:
            total += mid//t

        #심사 할수 있는 사람이 n 명 보다 많다면 왼쪽을 이분탐색해주고
        if total >= n:
            right = mid

        # n 명보다적게 심사를 할 수 있다면 오른쪽을 이분탐색 해 준다.
        else:
            left = mid + 1

    answer = right
    return answer
