class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != res[i]:
                count += 1
        
        return count
