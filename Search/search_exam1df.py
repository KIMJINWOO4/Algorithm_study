n = int(input())
array = list(map(int,input().split()))
m = int(input())
requ = list(map(int,input().split()))

def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
    return binary_search(array, target, start, end)
array.sort()
for i in range(m):
    a = binary_search(array,requ[i],0,n-1)
    if a == None:
        print("No",end = ' ')
    else:
        print("yes",end= ' ')

