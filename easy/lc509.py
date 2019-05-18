## Fibonacci numbers

# without cache, 17%
class Solution:
    def fib(self, N: int) -> int:
        def fibo(n):
            if n < 0:
                return None
            elif n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fibo(n-1) + fibo(n-2)
        return fibo(N)

# with cache, 85%
class Solution:
    def fib(self, N: int) -> int:
        cache = {}
        def helper(n):
            if n in cache:
                result = cache[n]
            elif 0 <= n < 2:
                result = n
            else:
                result = helper(n-1) + helper(n-2)

            cache[n] = result
            return result
        return helper(N)
