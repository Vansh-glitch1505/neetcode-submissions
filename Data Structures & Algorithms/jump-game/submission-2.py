class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        i = 0

        while i < len(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            i += 1
        
        return True