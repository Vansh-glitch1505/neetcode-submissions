class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            res.append(abs(num))
        res.sort()

        for i in range(len(res)):
            res[i] = res[i]*res[i]
        
        return res