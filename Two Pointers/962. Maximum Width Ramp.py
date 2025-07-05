class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        #intuition : to eliminate safely an element at certain index we need to guarantee that everything to right of it is smaller
        #pre-processing to include max_right array
        max_right = [0] * len(nums)
        i = len(nums)-1
        prev_max = 0
        for n in reversed(nums):
            max_right[i] = max(n,prev_max)
            prev_max = max_right[i]
            i -= 1

        #now apply two-pointer (window approach)
        l = 0
        res = 0
        for r in range(len(nums)):
            while nums[l] > max_right[r]:
                l += 1
            res = max(res, r -l)
        return res    
