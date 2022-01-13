import time

n, m = map(int,input().split())
x, y, d = map(int,input().split())
dir = [[0]*m for _ in range(n)]
dir[x][y] = 1
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))
dx = [-1,0,1,1]
dy = [0,1,0,-1]

def turn():
    global d
    d -= 1
    if d == -1:
        d = 3
#시작
count = 1
turn_time = 0
while True:
    turn()
    nx = x + dx[d]
    ny = y + dy[d]
    if dir[nx][ny] == 0 and data[nx][ny] == 0:
        dir[nx][ny] = 1
        x = nx
        y = ny
        turn_time = 0
        count += 1
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if data[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)



