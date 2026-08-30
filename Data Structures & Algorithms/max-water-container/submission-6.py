class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = maxProd = 0
        r = len(heights) - 1

        while l < r:
            space = r - l
            prod = min(heights[l], heights[r]) * space
            maxProd = max(maxProd, prod)

            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                l += 1
                r -= 1
        
        return maxProd