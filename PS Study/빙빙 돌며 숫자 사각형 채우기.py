rows,columns = map(int,input().split())

mat = [[0]*columns for _ in range(rows)]
r,c = 0,0
mat[r][c] = 1
dx,dy = [1,0,-1,0],[0,1,0,-1]
d = 0
def inrange(r,c):
    return 0<=r<rows and 0 <=c < columns

for i in range(2,rows*columns+1):
    nr,nc = r+dy[d],c+dx[d]
    if not inrange(nr,nc) or mat[nr][nc] != 0:
        d = (d+1) % 4
        nr,nc = r+dy[d],c+dx[d]
    mat[nr][nc] = i
    r,c = nr,nc

for row in mat:
    print(row)