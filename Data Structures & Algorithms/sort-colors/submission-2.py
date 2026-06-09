class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res0 = []
        res1 = []
        res2 = []

        for num in nums:
            if num == 0:
                res0.append(num)
            elif num == 1:
                res1.append(num)
            else:
                res2.append(num)        
        
        nums[:] = res0 + res1 + res2