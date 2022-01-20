from random import randint
import time

array = []
for _ in range(10000):
    array.append(randint(1,100))
start = time.time()
for i in range(len(array)):
    min = i
    for j in range(i-1,len(array)):
        if array[min] > array[j] :
            min = j
        array[i], array[min] = array[min], array[i]
end = time.time()
print(end-start)
array = []
for _ in range(10000):
    array.append(randint(1,100))
start = time.time()
array.sort()
end = time.time()
print(end-start)
