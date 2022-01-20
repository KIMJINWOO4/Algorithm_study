import time

n = input()
start = time.time()
row = int(n[1])
col = int(ord(n[0])) - int(ord('a')) + 1

step_t = [(-2,1),(-2,-1),(2,-1),(2,1),(1,2),(-1,2),(1,-2),(-1,-2)]
result = 0

for step in step_t:
    nx = row + step[0]
    ny = col + step[1]
    if nx >= 1 and nx <= 8 and ny >= 1 and nx <= 8:
        result += 1
end = time.time()
print(result,"\n",end-start)