

# input = 3
# input = 9
# input = 27
#

# def printstar(n):
#     if n == 3:
#         print('*'*3)
#         print()
#         print('* *')
#         print('*'*3)
#
#
#     printstar(n//3)


a = [[0,0,0],[0,1,0],[0,0,0]]
a[0] = a[0]*3
a[1] = a[1]*3
a[2] = a[2]*3
a = a*3
print(len(a))
# for i in range(len(a)//3,2*len(a)//3):
#     for j in range(len(a)//3,2*len(a)//3):
#         print(a)
for i in range(len(a)):
    print(a[i])