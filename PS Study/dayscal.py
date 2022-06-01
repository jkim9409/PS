m1,d1,m2,d2 = map(int,input().split())

monthday = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}
days1 = d1
days2 = d2
for i in range(1,m1):
    days1 += monthday[i]
for i in range(1,m2):
    days2 +=monthday[i]


days = days2-days1
while days < 0:
    days += 7

week = {
    0:'Mon',
    1:'Tue',
    2:'Wed',
    3:'Thu',
    4:'Fri',
    5:'Sat',
    6:'Sun',
}

print(week[days%7])