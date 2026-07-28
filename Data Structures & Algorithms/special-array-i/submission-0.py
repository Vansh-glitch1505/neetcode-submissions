class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        parity = False
        for i in range(len(nums)-1):
            if nums[i] % 2 == 0:
                parity = True
            else:
                parity = False
            if parity == True:
                if nums[i+1] % 2 == 0:
                    return False
            else:
                if nums[i+1] % 2 != 0:
                    return False
        
        return True