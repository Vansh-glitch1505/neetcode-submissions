class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i in range(len(s)):
            seen[s[i]] = 1 + seen.get(s[i], 0)
        
        for i, n in enumerate(s):
            if seen[n] == 1:
                return i
        
        return -1