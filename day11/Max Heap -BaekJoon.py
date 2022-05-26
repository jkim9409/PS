a = [1,2,3,4,5]
b = [3,4,5]
for i in range(len(a)):
    if a[i] == b[0] and a[i:i+len(b)] == b:
        print('True')
    else:
        print('False')