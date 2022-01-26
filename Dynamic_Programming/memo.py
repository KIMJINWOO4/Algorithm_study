n, m = map(int,input().split())
o = []
for _ in range(n):
    o.append(int(input()))
array = [10001] * (m+1)

array[0] = 0
for i in range(n):
    for j in range(o[i],m+1):
        if array[j-o[i]] != 10001:
            array[j] = min(array[j],array[j-o[i]]+1)
if array[m] == 10001:
    print(-1)
else:
    print(array[m])

