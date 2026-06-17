class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        res = -1

        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        for num in freq:
            if num == freq[num]:
                res = max(res, freq[num])
        
        return res
        