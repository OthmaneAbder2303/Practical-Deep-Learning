import time

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fib2(n, d):
    if n in d:
        return d[n]
    else :
        d[n] = fib2(n-1, d) + fib2(n-2, d)
        return d[n]

print("Normal Fibonacci calculation:")
start = time.time()
print(fib(40))
end = time.time() - start
print(end)

print("Dynamic Fibonacci calculation:")
d = {0:0, 1:1}
start = time.time()
print(fib2(40, d))
end = time.time() - start
print(end)