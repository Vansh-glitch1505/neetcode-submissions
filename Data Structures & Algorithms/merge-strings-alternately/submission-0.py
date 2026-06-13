class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1 = 0
        i2 = 0
        len1 = len(word1)
        len2 = len(word2)

        res = []

        while i1 < len1 and i2 < len2:
            res.append(word1[i1])
            res.append(word2[i2])
            i1 += 1
            i2 += 1

        while i1 < len1:
            res.append(word1[i1])
            i1 += 1

        while i2 < len2:
            res.append(word2[i2])
            i2 += 1

        return "".join(res)