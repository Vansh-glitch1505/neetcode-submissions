class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        count = 0
        maxCount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                maxCount = max(maxCount, count) 
                count = 0
        maxCount = max(maxCount, count)
        return maxCount