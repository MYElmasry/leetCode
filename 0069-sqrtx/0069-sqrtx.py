class Solution:
    def mySqrt(self, x: int) -> int:
        l= 1
        r = x
        if x <2:
            return x
        while l < r:
            mid = (l+r)//2
            if mid*mid == x:
               return mid
            if mid*mid > x:
                r = mid
            else:
                l = mid +1
        return l-1