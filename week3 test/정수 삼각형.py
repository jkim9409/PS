
# triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
def solution(triangle):
    # triangle의 두번째 열부터 계속 최대값으로 업데이트 해 주고, 마지막에 가장 마지막 열 에있는 값들중 최댓값을 구한다.
    # for 문은 1번째 인덱스 부터 시작하며, 이전의 열에 있는 원소들을 가져와 계속 더해줄 것이다.
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            # 각 열의 맨 좌측과 맨 우측은, 최댓값 비교가 필요 없이 삼각형의 전 row 에서 각각 맨 왼쪽, 오른쪽의 값만 더해준다.
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
                continue
            if j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][-1]
                continue
            # 종이에 그려보며 규칙을 찾았는데, 삼각형의 이전 row 의 index 와 index-1 값중 최댓값을 더해주면 된다.
            triangle[i][j] = triangle[i][j] + max(triangle[i-1][j-1],triangle[i-1][j])

    answer = max(triangle[-1])
    return answer

print(solution(triangle))