class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        res = [0]
        def getSum(n):
            sum = 0
            for digit in str(n): 
              sum += int(digit)      
            return sum
        for i in range(1, n+1):
            binary = bin(i).replace("0b", "")
            res.append(getSum(binary))
        return res