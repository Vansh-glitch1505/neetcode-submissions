class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            Ltotal = sum(nums[:i])
            Rtotal = sum(nums[i+1:])

            if Ltotal == Rtotal:
                return i

        return -1