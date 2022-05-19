

def phoneNumbers(phone_book):
    hash  = {}                 #Hash를 만들어준다.
    for num in phone_book:     #각각의 전화번호들을 Hash의 키로 설정해주고 임이의 값을 지정해준다
        hash[num] = 0
    for num in phone_book:     # 해쉬의 key 들을 하나씩 돌며 자신의 앞글자들을 key 자체로 가지고 있는 번호가 있는지 확인한다
        prefix = ''              #새로운 key 로 loop 으로 넘어갈때마다 prefix를 초기화 시킨다
        for char in num:       # 각 key 마다 앞글자들을 늘려가면서 prefix에 저장을 하고 prefix와 같은 전화번호가 있느지 탐색한다.
            prefix += char
            if prefix in hash and prefix != num: # prefix를 번호로 가지고있는 key를 탐색한다. prefix loop 마지막에 자기자신을 탐색하는 경우는 제외한다.
                answer = False
                return answer
    answer = True              # 나의 prefix를 전화번호로 갖는 값을 찾지못하면 True 를 리턴한다.
    return answer

a = ["12","123","1235","567","88"]
print(phoneNumbers(a))

def phoneNumbers2(phone_book):
    for num in phone_book:
        comp = [x for x in phone_book if len(x) > len(num)] #phone_book에서 자신보다 길이가 긴 번호들만 추출한다.
        for i in comp: # 후보들중에 자신을 prefix로 가지고 있는 후보가 있는지 확인해준다 .
            if i.find(num) == 0: #prefix 이기때문에 자기 자신으로 시작하는 번호들을 찾아야한다.
                return False
    return True #찾지 못했다면 true 를 리턴


a = ["12","123","1235","567","88"]
print(phoneNumbers2(a))