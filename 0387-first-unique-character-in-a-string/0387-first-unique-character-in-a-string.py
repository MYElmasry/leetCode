class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq ={}
        for i in range(len(s)):
            if s[i] in freq.keys():
                freq[s[i]] += 1
            else:
                freq[s[i]] =1
        for i in freq:
            if freq[i] == 1:
                return s.index(i)
        return -1