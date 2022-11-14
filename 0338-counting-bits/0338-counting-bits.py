class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        res = [0]
        for i in range(1, n+1):
            while i > 0:
                arr.append(i % 2)
                i = i // 2
            res.append(sum(arr))
            arr = []
        return res