import time
import sys

def factorial(n):
    rpta = 1
    while n > 1:
        rpta *= n
        n -=1
    return rpta


def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial_r(n-1)


if __name__ == '__main__':
    n = 1000 
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(n + 10)
    print(sys.getrecursionlimit())

    start = time.time()
    factorial(n)
    end  = time.time()
    print(end - start)

    start = time.time()
    factorial_r(n)
    end = time.time()
    print(end - start)

