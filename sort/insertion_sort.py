array = [7,5,9,1,0,6,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print(array)