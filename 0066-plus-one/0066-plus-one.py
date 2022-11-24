class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        for i in digits:
            res *= 10
            res += i
        res += 1
        final = []
        while res:
            final.append(res % 10)
            res = res // 10
        return final[::-1]