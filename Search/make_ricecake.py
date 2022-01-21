n, m = map(int,input().split())
array = list(map(int,input().split()))
start = 0
end = max(array)
result = 0
while start <= end:
    sum = 0
    mid = (start+end)//2
    for i in array:
        if i > mid:
            sum += i-mid
    if sum < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)


