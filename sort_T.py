n = int(input())
data = []
for _ in range(n):
    i = int(input())
    data.append(i)
data.sort(reverse=True)
for i in range(len(data)):
    print(data[i],end=' ')

