class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = []
        for i in s:
            res.append(i[::-1])
        res = " ".join(res)
        return res