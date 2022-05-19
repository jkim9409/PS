def devlopFunction (progresses, speeds):
    answer = []
    n = 0 # 기능이 배포 되기까지의 일수
    readyfuncs = 0 # 배포 준비가 완료된 기능 개수

    while len(progresses) > 0:
        if (n * speeds[0] + progresses[0]) >= 100: # 첫번째 작업물이 완료 되어야만 if 문에 들어오고, 들어와서 pop을 해주게된다. 다음작업물도 완료된 상태라면 다시한번 다시한번 if 문으로 들어와 같은 과정을 반복!
            readyfuncs += 1                 # 배포준비가 된 기능의 숫자가 증가한다
            progresses.pop(0)               # 배포준비가 된 기능들은 리스트에서 제외시킨다
            speeds.pop(0)                   # 배포준비가 된 기능들은 리스트에서 제외시킨다

            if len(progresses) == 0:       # 마지막 적업일 때는 readyfuncs 를 answer에 append 해주지 않으므로 따로 처리해준다.
                answer.append(readyfuncs)

        else:                       # 리스트의 첫번째 기능이 배포준비가 안되었다면, 배포준비된 기능들만 모아서 배포를 시작한다.
            if readyfuncs > 0:
                answer.append(readyfuncs) # 함께 배포될 기능의 숫자를 종합하여 배포시킨다.
                readyfuncs = 0     # 함께 배포될 기능들의 숫자가 초기화 된다
            n += 1                 # 작업물이 완료될때까지의 시간을 세준다.

    return answer

a = [95, 90, 99, 99, 80, 99]
b = [1, 1, 1, 1, 1, 1]

print(devlopFunction(a,b))