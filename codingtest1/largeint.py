import time
n, m, k = map(int,input().split())
data = list(map(int,input().split()))
start = time.time()
first = data[n-1]
sec = data[n-2]

result = 0
while True:
    for i in range(k):
        if m == 0:
            break;
        result += first
        m -= 1
    if m == 0:
        break
    result += sec
    m -= 1
end = time.time()
print(result)
print(end-start)