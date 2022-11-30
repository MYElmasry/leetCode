class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        chars = {}
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in chars:
               if s[i] != chars[pattern[i]]:
                    return False
            else:
                if s[i] in chars.values():
                    return False
                chars[pattern[i]] = s[i]
        return True