def sequential_search(n,target,array):
    for i in range(n):
        if target == array[i]:
            return print(i+1)
    print("not found")
input_data = input().split()
array = input().split()
n = int(input_data[0])
target = input_data[1]
sequential_search(n,target,array)
