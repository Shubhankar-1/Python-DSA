# 1 1 2 3 5 8 13 21 ....


from unittest import result


def fibonacci(n):
    if n <= 0:
        return 0

    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


fib_cache = {}


def fibonacci_cached(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1

    if n in fib_cache:
        return fib_cache[n]

    fib_cache[n] = fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

    return fib_cache[n]


def fibonacci_iterative(n):
    if n == 1 or n == 2:
        return 1
    previous = 0
    result = 1
    for i in range(n-1):
        result, previous = result + previous, result

    return result


print("Fibonacci normal - ", fibonacci(35))
print("Fibonacci Cached - ", fibonacci_cached(35))
print("Fibonacci iterative - ", fibonacci_iterative(35))
