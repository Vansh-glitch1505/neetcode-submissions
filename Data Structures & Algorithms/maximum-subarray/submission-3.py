class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total, maxTotal = nums[0], nums[0]

        for i in range(1, len(nums)):
            total = max(nums[i], total + nums[i])
            maxTotal = max(maxTotal, total)
        
        return maxTotal