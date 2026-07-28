class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = []
        count = 0
        for i in range(len(heights)):
            res.append(heights[i])
        
        res.sort()
        for i in range(len(heights)):
            if heights[i] != res[i]:
                count += 1
        
        return count
