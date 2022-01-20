def binary_search(array,target,start,end):
    while not start > end:
        mid = (start+end)//2
        if array[mid] == target:
            return print(mid+1)
        if array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return print("None")

n, target = map(int,input().split())
array = list(map(int,input().split()))
binary_search(array,target,0,n-1)
