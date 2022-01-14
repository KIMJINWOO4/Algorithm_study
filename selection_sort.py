array = [7,5,9,1,0,6,8]

for i in range(len(array)):
    min_x = i
    for j in range(i+1,len(array)):
        if array[min_x] > array[j]:
            min_x = j
    array[i], array[min_x] = array[min_x], array[i]

print(array)