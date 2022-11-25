class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charMap = {}
        if len(set(s)) != len(set(t)):
            return False
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in charMap:
                    if charMap[s[i]] != t[i]:
                        return False
                else:
                    charMap[s[i]] = t[i]
            return True
        else:
            return False