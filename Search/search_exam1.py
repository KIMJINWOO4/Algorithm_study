import time
n = int(input())
array = list(map(int,input().split()))
m = int(input())
requ = list(map(int,input().split()))
for i in range(m):
    for j in range(n):
        if requ[i] == array[j]:
            print("yes",end=' ')
            break
        elif j == (n-1):
            print("no",end=' ')
            break
