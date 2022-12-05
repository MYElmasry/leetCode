class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for i in words[0]:
            check = True
            for j in range(1, len(words)):
                if i in words[j]:
                    words[j] = words[j][:words[j].index(i)] + words[j][words[j].index(i)+1:]
                else:
                    check = False
            if check:
               res.append(i)
        return res