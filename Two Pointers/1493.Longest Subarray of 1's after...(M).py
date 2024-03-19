class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,countZero,maximum = 0 , 0 , 0
        for r in range(len(nums)):
            if not nums[r]:
                countZero += 1
            while countZero > 1:
                if not nums[l]:
                    countZero -= 1
                l += 1    
            maximum = max(maximum,r-l)
        return maximum        
