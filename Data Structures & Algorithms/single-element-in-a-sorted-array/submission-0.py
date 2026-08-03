class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
        
        for key, value in freq.items():
            if value == 1:
                return key