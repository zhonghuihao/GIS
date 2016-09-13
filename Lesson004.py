from module import trace
from module import memoize


@trace  # Trace the function
def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(4))
fib = memoize(fib)
print(fib(4))


