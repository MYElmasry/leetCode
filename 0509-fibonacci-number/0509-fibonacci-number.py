class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            l, r = 0, 1
            i = 2
            while i <= n:
                l, r = r, l+r
                i+=1
            return r