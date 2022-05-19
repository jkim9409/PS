def letterCombinations(digits: str) -> [str]:
    dict = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    # 처음부터 digits이 비어있으면 재귀함수로 돌아가지 않고 빈 리스트를 return 한다.
    if not digits:
        return []

    # 완성된 조합들을 append 해서 담아줄 빈 리스트를 생성한다.
    result = []

    # 재귀 함수를 만든다:
    # 먼저 반복해야될 부분을 찾는다.
    # 반복해야 될 부분은 : 딕셔너리에서 digit 에 상응하는 경우의수 를 찾고, path 에저장해주고 이 path 와 다음숫자를 인자값으로 준다.
    # 예를들어, 첫번째 반복에서는 digits = '23' 에서 0번째 인덱스인 2 의 pair인 'abc' 를 찾고 a 를 path 에 저장한다.
    #         그리고 다음 digit 인 3 과 path = 'a' 를 재귀함수의 인자값으로 주게된다
    def dfs(index,path):

        # 백트래킹: 답이 될수없는 후보를 탐색하지 않고 돌아가게 만드는 조건을 주는일.
        #        백트랙킹은 흔히 DFS 탐색중 가지치기를 해서 해당 노드를 더이상 탐색하지 않을때 부모 노드로 돌아가게 해주는역활을 하는데
        #        이 경우에 조합의 길이가 digits의 길이와 같아지면 해당 path 의탐색을 종료하고 조합들을 저장해서 result에 담아준다.
        #        if문 에서 return 은 재귀함수를 호출하기 바로 전 으로 돌아가며 재귀를 빠져나오는데, 이때 return 을 하면서 path에 마지막으로 담은 알파벳은 사라지며 이전 노드로 돌아간다.
        #

        if len(path) == len(digits):
            result.append(path)
            return

        for i in range(index,len(digits)):   # for 문의 index i 는 계속 증가하는동안
            for j in dict[digits[i]]:        # 다음 for 문의 j 는 계속 'abc','def','ghi' 등의 첫번째만 가르키게된다.
                dfs(i+1, path+j)

    dfs(0, '')
    return result

print(letterCombinations('23'))