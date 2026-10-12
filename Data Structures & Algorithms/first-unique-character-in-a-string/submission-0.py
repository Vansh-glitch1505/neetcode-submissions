class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        cap = True

        for i in range(len(s)):
            freq[s[i]] = 1 + freq.get(s[i], 0)
        
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i
        
        return -1