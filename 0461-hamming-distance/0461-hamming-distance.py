class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        if len(x) > len(y):
            while len(x) > len(y):
                y = '0'+ y
        elif  len(x) < len(y):
            while len(x) < len(y):
                x = '0' + x
        result = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                result += 1
        return result