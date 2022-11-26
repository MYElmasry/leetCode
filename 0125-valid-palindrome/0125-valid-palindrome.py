class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for i in s:
            if i.isalpha() == False and i.isdecimal() == False:
                s = s[:s.index(i)] + s[s.index(i)+1:]
        if s == s[::-1]:
            return True
        return False