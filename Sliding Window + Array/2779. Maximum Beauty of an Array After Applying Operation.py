class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        #sorting to manage intervals (ranges)
        nums.sort()
        res = 0     #max size of sliding window
        l = 0 
        for r in range(len(nums)):
            #reason behind 2*k is that we can add k to left pointer and subtract k from right
            #even if the gap is not covered we need to shift the left pointer
            while nums[r] - nums[l] > 2*k:
                l += 1
            res = max(res, r -l + 1)    
        return res       