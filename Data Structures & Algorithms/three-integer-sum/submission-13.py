class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):

            # Since array is sorted, no 3 numbers can sum to 0 after this
            if a > 0:
                break

            # Skip duplicate first elements
            if i > 0 and a == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1

                elif threeSum < 0:
                    l += 1

                else:
                    res.append([a, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # Skip duplicates on the left
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicates on the right
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res