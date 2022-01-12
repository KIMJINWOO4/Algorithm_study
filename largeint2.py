import time
n, m, k = map(int,input().split())
data = list(map(int,input().split()))
start = time.time()
data.sort()
first = data[n-1]
sec = data[n-2]

count = int(m//(k+1))*k
count += m % (k+1)

result = 0
result += count * first
result += m//(k+1) * sec
end = time.time()
print(result)
print(end-start)