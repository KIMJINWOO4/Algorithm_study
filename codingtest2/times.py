import time
n = int(input())
count = 0
start = time.time()
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
end = time.time()
print(count,"\n",end-start)