class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        res = 0
        prefixSum = {0 : 1}

        for num in nums:
            total += num
            diff = total - k

            res += prefixSum.get(diff, 0)
            prefixSum[total] = 1 + prefixSum.get(total, 0)
        
        return res