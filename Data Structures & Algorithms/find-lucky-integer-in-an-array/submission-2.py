class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        for num in freq:
            if num == freq[num]:
                res = max(res, num)
        
        return res