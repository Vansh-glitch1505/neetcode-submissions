class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        maxLen = 0

        for i in range(len(nums)):
            count[nums[i]] += 1
            if maxLen < count[nums[i]]:
                res = nums[i]
                maxLen = count[nums[i]]
            
        
        return res