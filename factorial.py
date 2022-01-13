import time
def fact_r(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
start = time.time()
print(fact(5))
end = time.time()
print((end-start)*1000)
start = time.time()
print(fact_r(5))
end = time.time()
print((end-start)*1000)