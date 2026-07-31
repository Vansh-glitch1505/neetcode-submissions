class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count = {}

        for num in nums:
            res += count.get(num, 0)
            count[num] = 1 + count.get(num, 0)
        
        return res