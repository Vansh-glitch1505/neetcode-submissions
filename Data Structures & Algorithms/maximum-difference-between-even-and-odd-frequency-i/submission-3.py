class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        maxOdd = 0
        minEven = float('inf')

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1


        for count in freq.values():
            if count % 2 == 0:
                minEven = min(minEven, count)
            else:
                maxOdd = max(maxOdd, count)

        return maxOdd - minEven