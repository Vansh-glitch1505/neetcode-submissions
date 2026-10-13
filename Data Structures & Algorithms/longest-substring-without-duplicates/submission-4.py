class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l, r = 0, 0
        freq = set()

        for r in range(len(s)):
            while s[r] in freq:
                freq.remove(s[l])
                l += 1
                
            freq.add(s[r])
            length = max(length, r - l + 1)
        
        return length