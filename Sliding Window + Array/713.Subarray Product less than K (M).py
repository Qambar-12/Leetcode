class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #sliding window solution where total number of subarrays are n(n-1)(n-2)...1 = n!
        #for each starting element left pointer we have n subarrays till right pointer
        l,res = 0,0
        prod = 1
        for r in range(len(nums)):
            prod *= nums[r]
            while l <= r and  prod >= k:
                prod //= nums[l]
                l += 1
            res += (r-l+1)    
        return res    
