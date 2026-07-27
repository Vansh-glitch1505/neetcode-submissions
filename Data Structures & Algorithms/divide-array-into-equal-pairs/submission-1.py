class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums)%2 != 0:
            return False
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
        for value in freq.values():
            if value%2 != 0:
                return False
        
        return True
