class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Base case: if the array is empty, your range(1, len(nums)) won't run,
        # but we should handle it just in case.
        if not nums:
            return 0

        # 1. Your exact logic: start with the first element and find uniques
        res = [nums[0]]  
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            res.append(nums[i])

        # 2. THE FIX: Overwrite the original 'nums' array with your 'res' array
        nums[:] = res  

        # 3. Return the length of your result, just like you did
        return len(res)