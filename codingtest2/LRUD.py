import time
n = int(input())
x, y = 1, 1
plan = input().split()
plan_t = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for a in plan:
    for i in range(len(plan_t)):
        if a == plan_t[i]:
            mx = x + dx[i]
            my = y + dy[i]
    if mx < 1 or mx > n or my < 1 or my > n:
        continue
    x, y = mx, my

print(x,y)