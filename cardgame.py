n, m = map(int,input().split())
result = 0
for _ in range(n):
        data = list(map(int,input().split()))
        min_v = min(data)
        result = max(min_v,result)
print(result)